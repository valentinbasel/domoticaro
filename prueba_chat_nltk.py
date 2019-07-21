#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#  pruebas con NLTK para el chatbot
###############################################################################

from nltk.corpus import wordnet as wn
from bot.chatbot import CHATBOT
from bot.eliza import ELIZA
import random
import time

def buscar_sinonimos(arg):
    synonyms = []
    texto = arg.lower()
    for syn in wn.synsets(texto,lang = "spa"):
        for lemma in syn.lemmas('spa'):
            synonyms.append(lemma.name())
    return synonyms

def start():
    c.mensaje("buscador de sinonimos, escribe cualquier palabra y yo te dire los sinonimos que encuentre.")

def recibir():
    cadena = c.mensaje_usuario()
    res=buscar_sinonimos(cadena.lower())
    if res != []:
        for mensa in res:
            c.mensaje(mensa)
            time.sleep(1)
        c.mensaje("listo 😬 ")
    else:
        c.mensaje("no encontre sinonimos para " + cadena)
        mensa = eli.analyze(cadena.lower())
        c.mensaje(mensa)
eli=ELIZA()
c = CHATBOT("TOKEN")
c.ordenes["start"]=start
c.recibir(recibir)
c.bucle_espera()
