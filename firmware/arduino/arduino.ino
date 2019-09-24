
int input;
char caracter;
int RELE[]={LOW,LOW,LOW,LOW};
String cadena;
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);

}



void comparo()
{
  if(cadena[0]=='r')
    {

      rele();
     return;
    }

}

void rele()
{
 
    {
      switch(cadena[1])
        {
        case '1':
          rele_estado(0);
          break;
        case '2':
          rele_estado(1);
          break;
        case '3':
          rele_estado(2);
          break;
        case '4':
          rele_estado(3);
          break;
        default:
          break;
        }
    }
}

void rele_estado(int port)
{

  if (cadena[2]=='1')
    {
    RELE[port]=1;
        Serial.println("1\n");

    return;
    }
  if (cadena[2]=='0')
    {
    RELE[port]=0;
    Serial.println("0\n");
    return;
    }
  if (cadena[2]=='e')
    {
    if (RELE[port]==0)
      {
           Serial.println("0\n");
           
      }
    if (RELE[port]==1)
      {
             Serial.println("1\n");
         
      }
    return;
    }

  
    Serial.println("err\n");
}
void actualizo_rele()
{
digitalWrite(13, RELE[0]); 
digitalWrite(12, RELE[1]); 
digitalWrite(11, RELE[2]); 
digitalWrite(10, RELE[3]); 
}
void loop() {
if (Serial.available()>0){
       cadena=Serial.readStringUntil('\n');
       comparo();
         }
        actualizo_rele();

}

