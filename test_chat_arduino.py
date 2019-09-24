#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# prueba de chat para domoticaro, saundo ELIZA y telegram
#
# Copyright © 2019 Valentin Basel <valentinbasel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

from bot.chatbot import CHATBOT
from bot.eliza import ELIZA
import random
from os import listdir
from os.path import isfile, join
import domoticaro
import time 
casa = domoticaro.iniciar("arduino")
casa.hardware.iniciar("/dev/ttyACM0")
rele1 = casa.hardware.Rele_1
rele2 = casa.hardware.Rele_2 
rele3 = casa.hardware.Rele_3
rele4 = casa.hardware.Rele_4

def ayuda():
    c.mensaje("soy un bot que puede enviar memes")
def start():
    c.mensaje("comencemos a usar nuestro super chatbot 2")

    print("usuario:",c.user_id())

    c.enviar_img("/home/vbasel/github/domoticaro/python.png")

def recibir():
    cadena = c.mensaje_usuario()
    cadena = cadena.lower()
    if cadena.find("prendo") >=0:
        c.mensaje("henciendo led")
        casa.hardware.Rele_1.on()

    elif cadena.find("apago") >=0:
        c.mensaje("apago led")
        casa.hardware.Rele_1.off()

    else:
        mensa=eli.analyze(cadena.lower())
        c.mensaje(mensa)

eli=ELIZA()
c = CHATBOT("652982145:AAH8Nb15GuXEbVtfGU4TGlhBNlFUEmr94vo")
c.ordenes["start"]=start
c.ordenes["help"]=ayuda


c.recibir(recibir)
c.bucle_espera()
