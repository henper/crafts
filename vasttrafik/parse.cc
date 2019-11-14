#include <iostream>
#include <ArduinoJson.h>

using namespace std;

int main()
{
  const size_t capacity = JSON_ARRAY_SIZE(20) + 21*JSON_OBJECT_SIZE(1) + JSON_OBJECT_SIZE(4) + 20*JSON_OBJECT_SIZE(18) + 11110;
  DynamicJsonDocument doc(capacity);

  DeserializationError result = deserializeJson(doc, cin);

  if (result != DeserializationError::Ok)
    cout << result.c_str();
  else
  {
    JsonArray departures = doc["DepartureBoard"]["Departure"];

    for (JsonObject departure : departures)
    {
      cout << departure["name"] << departure["time"] << "\n";
    }
  }
  
  return result == DeserializationError::Ok ? 0 : -1;
}