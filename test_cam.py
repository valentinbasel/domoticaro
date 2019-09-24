#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import domoticaro
import time 
robot = domoticaro.iniciar(None)

#color=[[49,50,50],[80, 255, 255]]
while(True):
    robot.camara.tomar_imagen()
    #x,y,w,h = robot.camara.detectar_rostro()
    #x,y,w,h = robot.camara.detectar_color(color=color)

    robot.camara.mostrar()
    robot.camara.esperar()
