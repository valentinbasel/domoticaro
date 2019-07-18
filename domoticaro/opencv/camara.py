#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# -camara.py-
# Copyright © 2017 valentinbasel@gmail.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
import numpy as np
import cv2
import time

class CAM(object):
    """ Class doc """

    def __init__ (self,cam=0):
        """ Class initialiser """
        self.dispositivo=cv2.VideoCapture(cam)
        self._Imagen=0
        self._ImagenOriginal=0

    def tomar_imagen (self):
        """ Function doc """
        (ok, self._Imagen) = self.dispositivo.read()
        self._ImagenOriginal=self._Imagen
        return self._Imagen

    def mostrar (self,nombre="camara",img=None):
        """ Function doc """
        if img==None:
            img=self._ImagenOriginal
        cv2.imshow(nombre,img)

    def detectar_rostro (self,img=None):
        """TODO: Docstring for detectar_rostro.
        :returns: TODO

        """
        rostro = "/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml"
        RostroCascada = cv2.CascadeClassifier(rostro)
        self.convertir_gris()
        faces = RostroCascada.detectMultiScale(
                self._Imagen,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags =cv2.CASCADE_SCALE_IMAGE
                )
        if faces != ():
            for (x, y, w, h) in faces:
                cv2.rectangle(
                            self._ImagenOriginal,
                            (x, y),
                            (x+w, y+h),
                            (0, 255, 0),
                            2
                            )
            return x,y,w,h
        else:
            return None,None,None,None
    def centro_cuadrado(self, x,y,w,h):
        """TODO: Docstring for centro_cuadrado.

        :x: TODO
        :returns: TODO

        """
        if x != None and y != None and w != None and h != None:
            centro_x=x+(w/2)
            centro_y=y+(h/2)
            cv2.rectangle(
                        self._ImagenOriginal,
                        (centro_x, centro_y),
                        (centro_x+2, centro_y+2),
                        (0, 0, 255),
                        2
                        )
            return centro_x, centro_y
        else:
            return None,None
    def convertir_gris (self,img=None):
        """ Function doc """
        if img==None:
            img=self._Imagen
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self._Imagen=gray
        return gray
    
    def espejar (self,img=None):
        """ Function doc """
        if img==None:
            img=self._Imagen
        invertido = cv2.flip( img, -1 )
        self._Imagen=invertido
        return invertido

    def convertir_umbral (self,img=None,minumb=0,maxumb=255):
        """ Function doc """
        if img==None:
            img=self._Imagen 
        flag,umb = cv2.threshold(img,minumb,maxumb,cv2.THRESH_OTSU)
        self._Imagen=umb
        return self._Imagen

    def detectar_color(self, color=0,img=None):
        """TODO: Docstring for detectar_color.

        :color: el valor del color HSV (min y max)
        :returns: x,y,w,h

        """
        if img==None:
            img=self._Imagen
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        color_minimo= np.array(color[0], dtype=np.uint8)
        color_maximo= np.array(color[1], dtype=np.uint8)
        #Crear una mascara con solo los pixeles dentro del rango de verdes
        mask = cv2.inRange(hsv, color_minimo, color_maximo)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2) 
        #Encontrar el area de los objetos que detecta la camara
        (_, cnts, _) = cv2.findContours(mask.copy(), 
                                        cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
        moments = cv2.moments(mask)
        area = moments['m00']
        if(area > 2000000):
            o = max(cnts, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(o)
            cv2.rectangle(
                            img,
                            (x, y),
                            (x+w, y+h),
                            (0, 255, 0),
                            2
                            )

            return x,y,w,h
        else:
            return None,None,None,None

    def esperar (self):
        """ Function doc """
        cv2.waitKey(1)
        time.sleep(0.025)
