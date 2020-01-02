#include<ESP8266WiFi.h>
#include<ESP8266WiFiMulti.h>
#include<ESP8266HTTPClient.h>

const char* ssid = "biggie"; //your WiFi Name
const char* password = "lusky_812";  //Your Wifi Password

const char* client_credentials = "NWpiZkVaQkRNQUpWUGpOWWFaUUZkQWl3aGZnYTpkOGlQVHJyUTNDZ2tmY21HcGNBRmw0NXBmU2Nh";
const char* device_id = "1";

const uint8_t finger_print[] = {0x7A, 0xF1, 0x5B, 0xEF, 0xDA, 0xF8, 0x14, 0xFA, 0x0D, 0x65, 0x38, 0x17, 0xD2, 0xC4, 0x5F, 0xE3, 0x76, 0x0B, 0x6F, 0xBD};

ESP8266WiFiMulti wifiMulti;

char validToken[1024] = "";
char* getValidToken()
{
  static int timestamp = 0;
  static int expiration = 0;

  if(millis() > timestamp + expiration)
  {
    Serial.println("Fetching new token..");

    std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
    client->setFingerprint(finger_print);
    HTTPClient https;
    
    //if(https.begin(*client, "https://api.vasttrafik.se", 443))
    if(https.begin(*client, "193.183.128.134", 443))
    {
      Serial.println("Connected to server");

      https.addHeader("Content-Type", "application/x-www-form-urlencoded");
      https.addHeader("Authorization", String("Basic ") + String(client_credentials));
      int httpCode = https.POST("/token");

      Serial.print("POST http-code: "); Serial.println(httpCode);
      
      Serial.println("Response:");
      String payload = https.getString();
      Serial.println(payload);

      https.end();
      Serial.println("\nDisconnected");

    }
    else
    {
      Serial.println(String("Connection to server failed"));
    }

    Serial.print("last ssl error: "); Serial.println(client->getLastSSLError());
  
    //char* buf[2048];
    //client->getLastSSLError(buf, sizeof(buf));
    //Serial.println(buf);

  }
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

  char* token = getValidToken();
  
}

void loop()
{
  if(wifiMulti.run() != WL_CONNECTED)
    return;
  
  Serial.println("Heartbeat!");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000);

  digitalWrite(LED_BUILTIN, LOW);
  delay(2000);
}
