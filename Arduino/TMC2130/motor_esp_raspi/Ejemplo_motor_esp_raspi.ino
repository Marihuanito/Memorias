
#define EN_PIN    13 //7  //Nano v3:    16 Mega:  38  //enable (CFG6)
#define DIR_PIN   26 //6  //            19        55  //direction
#define STEP_PIN  14 //5  //            18        54  //step
#define CS_PIN    5 //8 //            17        64  //chip select
#define MOSI_PIN  23
#define MISO_PIN 19
#define SCK_PIN  18

int stepDelay;
float steps = 200.0*16.0*4.0;
//bool finalcarrera_x = false;
#include <TMC2130Stepper.h>
TMC2130Stepper driver = TMC2130Stepper(EN_PIN, DIR_PIN, STEP_PIN, CS_PIN, MOSI_PIN, MISO_PIN, SCK_PIN);




void setup() {

  driver.begin();       // Initiate pins and registeries
  driver.rms_current(600);  // Set stepper current to 600mA. The command is the same as command TMC2130.setCurrent(600, 0.11, 0.5);
  driver.stealthChop(1);  // Enable extremely quiet stepping
  driver.microsteps(16); //configura micropasos hasta 256 (0,2,4,8,16,32,64,128,256)
  digitalWrite(EN_PIN, LOW);

  Serial.print("DRV_STATUS=0b");
  Serial.println(driver.DRV_STATUS(), BIN);
}

void loop() {
   
  stepDelay = 200;
  for (int i = 0; i <= 3200; i++) {
      digitalWrite(STEP_PIN, HIGH);
      delayMicroseconds(stepDelay);
      digitalWrite(STEP_PIN, LOW);
      delayMicroseconds(stepDelay);

   }
   
}
