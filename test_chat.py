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

def start():
    c.mensaje("comencemos a usar nuestro super chatbot")

def recibir():
    cadena = c.mensaje_usuario.lower()
    mensa=eli.analyze(cadena)
    c.mensaje(mensa)

eli=ELIZA()
c = CHATBOT("652982145:AAH8Nb15GuXEbVtfGU4TGlhBNlFUEmr94vo")
c.ordenes["start"]=start
c.recibir(recibir)
c.bucle_espera()
