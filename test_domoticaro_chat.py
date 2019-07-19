#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#  Prueba de domotica con el chat bot de TELEGRAM
###############################################################################

import domoticaro
import time 
from bot.chatbot import CHATBOT
from bot.eliza import ELIZA
import random

def start():
    c.mensaje("comencemos a usar nuestro super chatbot")

def recibir():
    cadena = c.mensaje_usuario.lower()
    if cadena.find("prender")>=0:
        if rele1.estado()==0:
            c.mensaje("prendo la luz")
            rele1.on()
        else:
            c.mensaje("l luz ya esta encendida")
    elif cadena.find("apagar")>=0:
        if rele1.estado()==1:
            c.mensaje("apago la luz")
            rele1.off()
        else:
            c.mensaje("la luz ya esta apagada")
    else:
        mensa=eli.analyze(cadena)
        c.mensaje(mensa)

casa = domoticaro.iniciar("icaro_cdc")
casa.hardware.iniciar("/dev/ttyACM0")
rele1 = casa.hardware.Rele_1

eli=ELIZA()
c = CHATBOT("652982145:AAH8Nb15GuXEbVtfGU4TGlhBNlFUEmr94vo")
c.ordenes["start"]=start
c.recibir(recibir)
c.bucle_espera()




# for t in range(17):
    # casa.hardware.Rele_1.conmutar()
    # print (rele2.conmutar())
    # print (rele3.conmutar())
    # print (rele4.conmutar())
    # time.sleep(3)
    
casa.hardware.cerrar()



