#include <Arduino.h>
#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ESP8266)
  #include <ESP8266WiFi.h>
#endif
#include <Firebase_ESP_Client.h>
#include<PulseSensorPlayground.h>

PulseSensorPlayground pulse;

//  Variables
const int PulseWire = 0; 
int var = 0;

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Insert your network credentials
#define WIFI_SSID "Realme"
#define WIFI_PASSWORD "t9kun6t7"

// Insert Firebase project API Key
#define API_KEY "AIzaSyDh0sX9rbp5LFJZZpW3lizxacws11CpqIs"

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://xerebro-28a99-default-rtdb.firebaseio.com/" 

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
bool signupOK = false;

void reciver(){
  int mag_val = analogRead(sensor);
  Serial.println(mag_val);
  delay(100);
}



void transmitter(){
  switch (var) {
    case 1:
      while(var = 1){
        pinMode(18, HIGH);
        delay(2000);
        pinMode(18, LOW);
        delay(2000);
      }
      // statements
    
    case 2:
      while(var == 2){
        int t1 = random(125,62.5);
        pinMode(18, HIGH);
        delay(t1);
        pinMode(18, LOW);
        delay(random(t1);
      }
        
    case 3:
      while(var ==3){
        int t2 = random(62.5,41.5);
        pinMode(18, HIGH);
        delay(t2);
        pinMode(18, LOW);
        delay(t2);
      }
        
  
    case 4:
      while(var == 4){
        int t3 = random(41.5,14.2);
        pinMode(18, HIGH);
        delay(t3);
        pinMode(18, LOW);
        delay(t3));
      }
       

    case 5:
      while(var == 5){
        pinMode(18, HIGH);
        delay(14.2);
        pinMode(18, LOW);
        delay(14.2);
      }
      
}
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  int count = 0;
  while (WiFi.status() != WL_CONNECTED){
    Serial.println(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
  // put your setup code here, to run once:

}

void loop() {
  if(rate > 60){
    reciver();
  }
  
  if(mag_val < ){
    var == 1;
  }
  if(mag_val >  || mag_val <  ){
    var == 2;
  }if(mag_val >   || mag_val <  ){
    var == 3;
  }if(mag_val >   || mag_val <  ){
    var ==4;
  }if(mag_val > || mag_val <  ){
    var == 5;
  }else(){
    Serial.println("Error 101 brain not found");
  }
  int rate = pulse.getBeatsPerMinute();
  if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis > 150 || sendDataPrevMillis == 0)){
  sendDataPrevMillis = millis();
    
    // On status
    if (Firebase.RTDB.setBool(&fbdo, "Devices/1001/STATUS", true)) {
        Serial.println("PASSED");
        Serial.println("PATH: " + fbdo.dataPath());
        Serial.println("TYPE: " + fbdo.dataType());
    }
    else {
        Serial.println("FAILED");
        Serial.println("REASON: " + fbdo.errorReason());
    }

    // Write an Int number on the database path test/int
    if (Firebase.RTDB.setInt(&fbdo, "Devices/1001/Rate", rate)){
      Serial.println("PASSED");
      Serial.println("PATH: " + fbdo.dataPath());
      Serial.println("TYPE: " + fbdo.dataType());
    }
    else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }
    
    // Write an Float number on the database path test/float
    if (Firebase.RTDB.setFloat(&fbdo, "test/float", random(70, 100))){
      Serial.println("PASSED");
      Serial.println("PATH: " + fbdo.dataPath());
      Serial.println("TYPE: " + fbdo.dataType());
      //Serial.println(BPM);
    }
    else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

  // put your main code here, to run repeatedly:
  }
}