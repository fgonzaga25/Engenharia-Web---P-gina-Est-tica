#define umidadeAnalogica 0  //Atribui o pino 0 a variável umidade - leitura analógica do sensor
#define LedAzul 4      //Atrubui o pino 4 a variável LedAzul
#define LedVermelho 5  //Atribui o pino 5 a variável LedVermelho
#define LedVerde 6     //Atribui o pino 6 a variável LedVerde

int valorumidade;  //Declaração da variável que armazenará o valor da umidade lida - saída analogica
int valorporcent;  //Declaa variável que armazena a porcentagem


#include <Wire.h>
#include <LiquidCrystal_I2C.h>
//Inicializa o display no endereco 0x27
LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
  Serial.begin(9600);                //Incia a comunicação serial
  pinMode(umidadeAnalogica, INPUT);  //Define umidadeAnalogica como entrada
  pinMode(LedVermelho, OUTPUT);      //Define LedVermelho como saída
  pinMode(LedVerde, OUTPUT);         //Define LedVerde como saída

  lcd.init();
}

void loop() {
  valorumidade = analogRead(umidadeAnalogica);  //Realiza a leitura analógica do sensor e armazena em valorumidade
  Serial.print("Analogico: ")
  Serial.println(valorumidade);
  valorumidade = map(valorumidade, 130, 280, 0, 100);
  //valorumidade = map(valorumidade, 410, 690, 0, 100); //Transforma os valores analógicos em uma escala de 0 a 100
  Serial.print("valor porcent ");

  if (valorumidade <= 1) {
    valorumidade = 0;
  }
  if (valorumidade >= 100) {
    valorumidade = 100;
  }
  Serial.println(valorumidade);

  if (valorumidade >= 20) {  //Se esse valor for igual a 0, será mostrado no monitor serial que o solo está úmido e o led verde se acende
    //Serial.println("Status: Solo úmido");
    digitalWrite(LedVermelho, LOW);
    digitalWrite(LedVerde, HIGH);
  } else {  // se esse valor for igual a 1, será mostrado no monitor serial que o solo está seco e o led vermelho se acende
    //Serial.println("Status: Solo seco");
    analogWrite(LedVermelho, HIGH);
    analogWrite(LedVerde, 0);
  }

  delay(1000);  //Atraso de 500ms
  lcd.clear();

  lcd.setBacklight(HIGH);
  lcd.setCursor(0, 0);
  lcd.print("Nivel agua");
  lcd.setCursor(0, 1);
  lcd.print("porcentagem: ");
  lcd.print(valorumidade);
  lcd.print("%");
}