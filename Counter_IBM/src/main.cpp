/**
 * Helloworld style, connect an ESP8266 to the IBM IoT Foundation
 *
 * Author:
 * License: Apache License v2
 */
#include <ESP8266WiFi.h>
#include <PubSubClient.h> // https://github.com/knolleary/pubsubclient/releases/tag/v2.3

//-------- Customise these values -----------
const char* ssid = "KOFUJI_2022";
const char* password = "b0r@b0r@";

#define ORG "ss4bdu"
#define DEVICE_TYPE "esp8266"
#define DEVICE_ID "esp1"
#define TOKEN "I42?dx6ddqIcw2ujmr"
//-------- Customise the above values --------

char server[] = ORG ".messaging.internetofthings.ibmcloud.com";
char topic[] = "iot-2/evt/status/fmt/json";
char authMethod[] = "use-token-auth";
char token[] = TOKEN;
char clientId[] = "d:" ORG ":" DEVICE_TYPE ":" DEVICE_ID;


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("callback invoked");
}

WiFiClient wifiClient;
PubSubClient client(server, 1883, callback, wifiClient);

void setup() {
  Serial.begin(115200);
  Serial.println();

  Serial.print("Connecting to ");
  Serial.print(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");

  Serial.print("WiFi connected, IP address: ");
  Serial.println(WiFi.localIP());
}

int counter = 0;

void loop() {

  if (!!!client.connected()) {
  Serial.print("Reconnecting client to ");
  Serial.println(server);
    while (!!!client.connect(clientId, authMethod, token)) {
      Serial.print(".");
      delay(500);
    }
  Serial.println();
  }

  String payload = "{'d':{'counter':";
  payload += counter;
  payload += "}}";

  Serial.print("Sending payload: ");
  Serial.println(payload);

  if (client.publish(topic, (char*) payload.c_str())) {
    Serial.println("Publish ok");
  } else {
    Serial.println("Publish failed");
  }

  ++counter;
  delay(10000);
}
