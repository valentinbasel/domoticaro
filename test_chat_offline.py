#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# test off-line de ELIZA
###############################################################################

from bot.eliza import ELIZA

chat = ELIZA()
print("empecemos a charlar")
while True:
    cadena = input("> ").lower()
    print(chat.analyze(cadena))


