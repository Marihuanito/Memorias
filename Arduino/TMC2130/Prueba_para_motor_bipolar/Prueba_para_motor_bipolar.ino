//prueba para hacer funcionar el motor con el TMC.

#define EN_PIN    13 //7  //Nano v3:    16 Mega:  38  //enable (CFG6)
#define DIR_PIN   26 //6  //            19        55  //direction
#define STEP_PIN  14 //5  //            18        54  //step
#define CS_PIN    5 //8 //            17        64  //chip select
#define MOSI_PIN  23
#define MISO_PIN 19
#define SCK_PIN  18

//#define FC_X 36 //Final de Carrera eje X

bool dir = true;
int stepDelay;
float steps = 200.0*16.0*4.0;
int var_aux2= 0;
//bool finalcarrera_x = false;
bool var_aux;
#include <TMC2130Stepper.h>
TMC2130Stepper driver = TMC2130Stepper(EN_PIN, DIR_PIN, STEP_PIN, CS_PIN, MOSI_PIN, MISO_PIN, SCK_PIN);

void setup() {
 // pinMode(FC_X, INPUT);
  Serial.begin(9600);
  //while(!Serial);
  //Serial.println("Start...");
  driver.begin();       // Initiate pins and registeries
  driver.rms_current(600);  // Set stepper current to 600mA. The command is the same as command TMC2130.setCurrent(600, 0.11, 0.5);
  driver.stealthChop(0);  // Enable extremely quiet stepping
  driver.microsteps(0); //configura micropasos hasta 256 (0,2,4,8,16,32,64,128,256)
  digitalWrite(EN_PIN, LOW);

  Serial.print("DRV_STATUS=0b");
  Serial.println(driver.DRV_STATUS(), BIN);
  var_aux=true;
  
}  



void loop() {
  /*
  digitalWrite(STEP_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(STEP_PIN, LOW);
  delayMicroseconds(10);
*/

   digitalWrite(DIR_PIN, HIGH);
   Serial.println(DIR_PIN);
   delay(2000);
   //Serial.println(driver.DRV_STATUS(), BIN);
   //digitalWrite(EN_PIN, LOW);
   while(var_aux == true){
   //driver.shaft_dir(1);
   stepDelay = 20;
   // Giramos 200 pulsos para hacer una vuelta completa
   Serial.println("Izd.:");
   //Serial.println(steps);
   //finalcarrera_x=digitalRead(FC_X);
   for (int i = 0; i <= 200; i++) {
      digitalWrite(STEP_PIN, HIGH);
      delayMicroseconds(stepDelay);
      digitalWrite(STEP_PIN, LOW);
      delayMicroseconds(stepDelay);
      //finalcarrera_x=digitalRead(FC_X);
      //Serial.println(i);
      delay(10);
   }
   
/*
   for (float x = 0.0; x < steps; x++) {
      digitalWrite(STEP_PIN, HIGH);
      delayMicroseconds(stepDelay);
      digitalWrite(STEP_PIN, LOW);
      delayMicroseconds(stepDelay);
   }
*/

   digitalWrite(DIR_PIN, LOW);
   delay(5000);
   Serial.print(DIR_PIN);
 
   
   driver.shaft_dir(0);
   stepDelay = 20;
   // Giramos 400 pulsos para hacer dos vueltas completas
   Serial.println("Dch.:");
   //Serial.println(steps);
   for (int j = 0; j <= 200; j++) {
      digitalWrite(STEP_PIN, HIGH);
      delayMicroseconds(stepDelay);
      digitalWrite(STEP_PIN, LOW);
      delayMicroseconds(stepDelay);
      //Serial.print("a");
      delay(10);
   }
   delay(2000);
   //digitalWrite(EN_PIN, HIGH);
   var_aux2++;
   if(var_aux2==10){
    var_aux= false;
   }
   }
   Serial.println("Salimos del loop");
   
}

   
  
