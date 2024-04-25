/*
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR: Andrés Villota Camacho                                      Enero/2021
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA:    División                             VERSIÓN:       1.0
//   DISPOSITIVO: ESP 32                               COMPILADOR:    AVR
//   Entorno IDE:   1.8.13                             SIMULADOR:     VIRTRONIC
//   TARJETA DE APLICACIÓN:                            DEBUGGER:     
////////////////////////////////////////////////////////////////////////////////////
División mediante sumas y restas. 
////////////////////////////////////////////////////////////////////////////////////
*/
///////////////////////////////////////////////////////////////////////////////////
// VARIABLES GLOBALES //////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////
int divisor;
int dividendo;
int resto;
float cociente;
int var_aux=0;
int contador=0;
int decimales;
float resultado=0;

////////////////////////////////////////////////////////////////////////////////////
// FUNCIONES ///////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////


void division(int dividendo, int divisor){

  cociente=0;
  var_aux=0;
  while (dividendo>var_aux){
  var_aux= var_aux + divisor;
  cociente++;
 }
 

 if(var_aux>dividendo){
  var_aux = var_aux - divisor;
  cociente--;
 }
 
 resto = dividendo-var_aux;
 
}

////////////////////////////////////////////////////////////////////////////////////
// CONFIGURACIÓN ///////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

////////////////////////////////////////////////////////////////////////////////////
// PRINCIPAL ///////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  Serial.print("dividendo: ");
  while (!Serial.available()){
    delay(500);
 }
 String str = Serial.readStringUntil('\n');
 dividendo = str.toInt();
 Serial.println(dividendo);

 Serial.print("Divisor: ");
  while (Serial.available()==0){
    delay(500);
 }
 str = Serial.readStringUntil('\n');
 divisor = str.toInt();
 Serial.println(divisor);


 Serial.println("Décimales deseados:");
  while (Serial.available()==0){
    delay(500);
 }
 str = Serial.readStringUntil('\n');
 decimales = str.toInt();
 int conteo_decimales=0;
 resultado=0;
 
 do{
  division(dividendo,divisor);

  if (resto > 0){
    resto = resto*10;
    dividendo=resto;
    }
  if (conteo_decimales==0){
    resultado= cociente;
    }
  else{
    
    cociente= cociente * (pow(10,(conteo_decimales*-1)));

    resultado= resultado+cociente;
  }

  conteo_decimales++;
 }while (resto>0 && conteo_decimales <= decimales);
  
 Serial.print("resultado: ");
 Serial.println(resultado, conteo_decimales-1); 

}
