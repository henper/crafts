#include<ESP8266WiFi.h>
#include<ESP8266WiFiMulti.h>
#include<ESP8266HTTPClient.h>

#include <ArduinoJson.h>
#include <string.h>

const char* ssid = "biggie"; //your WiFi Name
const char* password = "lusky_812";  //Your Wifi Password

const char* client_credentials = "NWpiZkVaQkRNQUpWUGpOWWFaUUZkQWl3aGZnYTpkOGlQVHJyUTNDZ2tmY21HcGNBRmw0NXBmU2Nh";
//const char* device_id = "1";


/* Fetch with command:
 * > curl --verbose -k -d "grant_type=client_credentials" -H "Authorization: Basic NWpiZkVaQkRNQUpWUGpOWWFaUUZkQWl3aGZnYTpkOGlQVHJyUTNDZ2tmY21HcGNBRmw0NXBmU2Nh" https://api.vasttrafik.se:443/token
 *
 * After wich the server certificate (starts with -----BEGIN CERTIFICATE----- and ends with -----END CERTIFICATE-----)
 * saved to the file 'cert.perm'. Command below used to create finger print from certificate:
 * > openssl x509 -noout -in ./cert.perm -fingerprint -sha1
 */
const uint8_t finger_print[] = {0x7A, 0xF1, 0x5B, 0xEF, 0xDA, 0xF8, 0x14, 0xFA, 0x0D, 0x65, 0x38, 0x17, 0xD2, 0xC4, 0x5F, 0xE3, 0x76, 0x0B, 0x6F, 0xBD};

ESP8266WiFiMulti wifiMulti;

static char* validToken = NULL;
static unsigned long expiration = 0;
char* getValidToken()
{
  // check if we already have a valid token
  if (millis() > expiration)
  {
    Serial.println("Fetching new token..");

    // if there was a previous token it has now expired and we can delete it
    if(validToken != NULL)
      free(validToken);

    std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
    client->setFingerprint(finger_print); //TODO: figure out how to fetch the certificate and create fingerprint programmatically
    HTTPClient https;

    if (!https.begin(*client, "https://api.vasttrafik.se/token"))
      return NULL; // TODO print SSL error?
    
    https.addHeader("Content-Type", "application/x-www-form-urlencoded");
    https.addHeader("Authorization", String("Basic ") + String(client_credentials));
    int httpCode = https.POST("grant_type=client_credentials&scope=1");  //device_id

    if (httpCode != 200)
    {
      Serial.println(String("HTTP Return code: ") + httpCode);
      return NULL;
    }

    const size_t capacity = 256; // arbitrarily chosen...
    DynamicJsonDocument json(capacity);
    String responseStr = https.getString(); //TODO use getStream() instaed
    Serial.println(responseStr);
    DeserializationError response = deserializeJson(json, responseStr);

    if (response != DeserializationError::Ok)
    {
      Serial.println(response.c_str());
      return NULL;
    }

    // fetch and save the token on the heap
    const char* tempToken = json["access_token"];
    if (tempToken == NULL)
    {
      Serial.println("Response did not include a token?");
      return NULL;
    }

    validToken = (char*)malloc(strlen(tempToken) + 1);
    strcpy(validToken, tempToken);

    unsigned long validity = json["expires_in"];
    expiration = millis() + validity * 1000;

    https.end();
  }

  Serial.print("token: "); Serial.println(validToken);
  Serial.print("expires in: "); Serial.println(expiration);

  return validToken;
}

void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  // verbose
  Serial.setDebugOutput(true);

  // connect to wifi
  Serial.println("Connecting ");
  WiFi.mode(WIFI_STA);
  wifiMulti.addAP(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Connected!");
  
}

void loop()
{
  if (wifiMulti.run() != WL_CONNECTED)
    return;
  
  Serial.println("Heartbeat!");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000);

  char* token = getValidToken();

  digitalWrite(LED_BUILTIN, LOW);
  delay(2000);
}
