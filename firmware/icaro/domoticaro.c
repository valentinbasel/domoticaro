
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include <__cdc.c>
#include <np05_06.h>
#define ANALOGREAD

#define LCDI2CHOME
#define LCDI2CINIT

#define LCDI2CCLEAR
#define LCDI2CSETCURSOR
#define LCDI2CNEWCHAR
//#define ANALOGREAD
#define LCDI2CBACKLIGHT
#define LCDI2CNOBACKLIGHT
#define LCDI2CPRINTF
#include<lcdi2c.h>
#include<lcdi2c.c>

unsigned char i;
unsigned char receivedbyte;
unsigned char rxstr[0]="";
int valor=0;
int caracter;
int RELE[3]={0,0,0,0};

void setup()
{
    TRISB=0;
    pinmode(21,INPUT);
    pinmode(22,INPUT);
    pinmode(23,INPUT);
    pinmode(24,INPUT);
    pinmode(25,OUTPUT);
    pinmode(26,OUTPUT);
    pinmode(27,OUTPUT);
    pinmode(28,OUTPUT);
    ServoAttach(8);
    ServoAttach(9);
    ServoAttach(10);
    ServoAttach(11);
    ServoAttach(12);
    PORTD=0;
    PORTB=0;
}

void LCD_CLEAR()
{
lcdi2c_home();
lcdi2c_clear();
CDCputs("1\n",2);
}

void LCD_SALTO()
{
	if (leo_puerto()==1)
		{
		if (caracter=='0')
			{
			lcdi2c_setCursor(0,0);
			CDCputs("1\n",2);
			return;
			}
		if (caracter=='1')
			{
			lcdi2c_setCursor(0,1);
			CDCputs("1\n",2);
			return;			
			}

		}
}
void LCD()
{
	while(caracter != '\n')
	{
	if (leo_puerto()==1)
		{
		if (caracter=='\n')
		{
			CDCputs("1\n",2);
			return;
		}
  		lcdi2c_backlight();
  		lcdi2c_printf(rxstr);
		}
	}
Delayus(100);
CDCputs("1\n",2);
}

void rele_estado(int port)
{
  if (leo_puerto()==1)
	{
	if (caracter=='1')
		{
		RELE[port]=1;
		CDCputs("1\n",2);
		return;
		}
	if (caracter=='0')
		{
		RELE[port]=0;
		CDCputs("0\n",2);
		return;
		}
	if (caracter=='e')
		{
		if (RELE[port]==0)
			{
	                CDCputs("0\n",2);
			}
		if (RELE[port]==1)
			{
	                CDCputs("1\n",2);
			}
		return;
		}

	}
CDCputs("er\n",3);
}

int leo_puerto()
{
while ((receivedbyte=CDCgets(rxstr))==0);
        rxstr[receivedbyte]=0;
        if (receivedbyte>0)
            {
             caracter=rxstr[0];
             return 1;
            }
        return 0;
}

void comparo()
{
  if(caracter=='r')
    {
      rele();
     return;
    }
   if(caracter=='a')
   {
     analogico();
     return;
   }
   if(caracter=='l')
   {
     LCD();
     return;
   }
   if(caracter=='L')
   {
     LCD_CLEAR();
     return;
   }
   if(caracter=='N')
   {
     LCD_SALTO();
     return;
   }
   if(caracter=='b')
    {
      //LCD();
      CDCputs("domoticaro \n",12);
     return;
    }
}
void snd_analogico(int val)
{
float valor=0;
unsigned char chaine[];

int i=0;
int tam=0;
valor=analogread(val);
x_ftoa(valor,chaine,2,2);
strcat(chaine,"\n");
tam=strlen(chaine);
CDCputs(chaine,tam);
}

void analogico()
{

  if(leo_puerto()==1)
   {
			switch(caracter)
				{
				case '1':
					snd_analogico(13);
					break;
				case '2':
					snd_analogico(14);
					break;
				case '3':
					snd_analogico(15);
					break;
				case '4':
					snd_analogico(16);
					break;
				default:
					CDCputs("er\n",3);
					break;
				}
   }
}



void rele()
{
	if (leo_puerto()==1)
		{
			switch(caracter)
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
					CDCputs("er\n",3);
					break;
				}
		}
}

void loop()
{
  lcdi2c_init(16,2,0x27);
  lcdi2c_home();
  Delayus(100);
  lcdi2c_backlight();
    while(1)
    {
      if(leo_puerto()==1)
         {
            comparo();
         }
        caracter=0;
        receivedbyte=0;
        PORTB=(16*RELE[0])+(32*RELE[1])+(64*RELE[2])+(128*RELE[3]);
    }
}