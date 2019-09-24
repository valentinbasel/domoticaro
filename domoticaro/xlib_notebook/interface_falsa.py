#!/usr/bin/env python
# -*- coding: utf-8 -*-

# interfacepc's name and a brief description.
# Copyright © 2017 valentin basel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
import Xlib.XK


class INTERFACES(object):

    # """MOUSE contiene los metodos necesarios para mover el puntero del
       # mouse por la pantalla"""
    # KEY_NAMES = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
     # ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
     # '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
     # 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
     # 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
     # 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
     # 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
     # 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
     # 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
     # 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
     # 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
     # 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     # 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
     # 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     # 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
     # 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
     # 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
     # 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
     # 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
     # 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
     # 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
     # 'command', 'option', 'optionleft', 'optionright']

    def __init__(self):
        """TODO: to be defined1. """
        self._display = Display(os.environ['DISPLAY'])
        self.mapa_botones_mouse = { 'izquierdo': 1,
                                    'medio': 2,
                                    'derecho': 3,
                                    1: 1,
                                    2: 2,
                                    3: 3,
                                    4: 4,
                                    5: 5,
                                    6: 6,
                                    7: 7}
        #self.__iniciar_teclado()

    # def __iniciar_teclado(self):
        # """TODO: Docstring for __iniciar_teclado.
        # :returns: TODO

        # """
        # self.keyboardMapping = dict([(key, None) for key in self.KEY_NAMES])
        # self.keyboardMapping.update({
            # 'backspace':         self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('BackSpace')),
            # '\b':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('BackSpace')),
            # 'tab':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Tab')),
            # 'enter':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Return')),
            # 'return':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Return')),
            # 'shift':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Shift_L')),
            # 'ctrl':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Control_L')),
            # 'alt':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Alt_L')),
            # 'pause':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Pause')),
            # 'capslock':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Caps_Lock')),
            # 'esc':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Escape')),
            # 'escape':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Escape')),
            # 'pgup':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Page_Up')),
            # 'pgdn':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Page_Down')),
            # 'pageup':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Page_Up')),
            # 'pagedown':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Page_Down')),
            # 'end':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('End')),
            # 'home':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Home')),
            # 'left':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Left')),
            # 'up':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Up')),
            # 'right':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Right')),
            # 'down':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Down')),
            # 'select':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Select')),
            # 'print':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Print')),
            # 'execute':           self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Execute')),
            # 'prtsc':             self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Print')),
            # 'prtscr':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Print')),
            # 'prntscrn':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Print')),
            # 'printscreen':       self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Print')),
            # 'insert':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Insert')),
            # 'del':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Delete')),
            # 'delete':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Delete')),
            # 'help':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Help')),
            # 'winleft':           self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Super_L')),
            # 'winright':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Super_R')),
            # 'apps':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Super_L')),
            # 'num0':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_0')),
            # 'num1':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_1')),
            # 'num2':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_2')),
            # 'num3':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_3')),
            # 'num4':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_4')),
            # 'num5':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_5')),
            # 'num6':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_6')),
            # 'num7':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_7')),
            # 'num8':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_8')),
            # 'num9':              self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_9')),
            # 'multiply':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Multiply')),
            # 'add':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Add')),
            # 'separator':         self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Separator')),
            # 'subtract':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Subtract')),
            # 'decimal':           self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Decimal')),
            # 'divide':            self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('KP_Divide')),
            # 'f1':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F1')),
            # 'f2':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F2')),
            # 'f3':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F3')),
            # 'f4':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F4')),
            # 'f5':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F5')),
            # 'f6':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F6')),
            # 'f7':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F7')),
            # 'f8':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F8')),
            # 'f9':                self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F9')),
            # 'f10':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F10')),
            # 'f11':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F11')),
            # 'f12':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F12')),
            # 'f13':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F13')),
            # 'f14':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F14')),
            # 'f15':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F15')),
            # 'f16':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F16')),
            # 'f17':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F17')),
            # 'f18':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F18')),
            # 'f19':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F19')),
            # 'f20':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F20')),
            # 'f21':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F21')),
            # 'f22':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F22')),
            # 'f23':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F23')),
            # 'f24':               self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('F24')),
            # 'numlock':           self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Num_Lock')),
            # 'scrolllock':        self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Scroll_Lock')),
            # 'shiftleft':         self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Shift_L')),
            # 'shiftright':        self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Shift_R')),
            # 'ctrlleft':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Control_L')),
            # 'ctrlright':         self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Control_R')),
            # 'altleft':           self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Alt_L')),
            # 'altright':          self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Alt_R')),
            # # These are added because unlike a-zA-Z0-9, the single characters do not have a
            # ' ': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('space')),
            # 'space': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('space')),
            # '\t': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Tab')),
            # '\n': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Return')),  # for some reason this needs to be cr, not lf
            # '\r': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Return')),
            # '\e': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('Escape')),
            # '!': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('exclam')),
            # '#': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('numbersign')),
            # '%': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('percent')),
            # '$': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('dollar')),
            # '&': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('ampersand')),
            # '"': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('quotedbl')),
            # "'": self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('apostrophe')),
            # '(': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('parenleft')),
            # ')': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('parenright')),
            # '*': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('asterisk')),
            # '=': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('equal')),
            # '+': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('plus')),
            # ',': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('comma')),
            # '-': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('minus')),
            # '.': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('period')),
            # '/': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('slash')),
            # ':': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('colon')),
            # ';': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('semicolon')),
            # '<': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('less')),
            # '>': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('greater')),
            # '?': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('question')),
            # '@': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('at')),
            # '[': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('bracketleft')),
            # ']': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('bracketright')),
            # '\\': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('backslash')),
            # '^': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('asciicircum')),
            # '_': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('underscore')),
            # '`': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('grave')),
            # '{': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('braceleft')),
            # '|': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('bar')),
            # '}': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('braceright')),
            # '~': self._display.keysym_to_keycode(Xlib.XK.string_to_keysym('asciitilde')),
            # })

            # # Trading memory for time" populate winKB so we don't have to call VkKeyScanA each time.
        # for c in """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890""":
            # self.keyboardMapping[c] = self._display.keysym_to_keycode(Xlib.XK.string_to_keysym(c))

    def mover(self, x,y):
        """mueve el puntero del mouse por la pantalla.
           sus parametors son:

        :x: valor X dentro de la pantalla
        :y: valor Y dentro de la pantalla
        :returns: True
        """
        if x != None and y != None:
            fake_input(self._display, X.MotionNotify, x=x, y=y) 
            self._display.sync()
            return True
        else:
            return False
    def mover_relativo(self, x,y):
        """mueve el puntero del mouse de forma relativa a su posición actual.

        :x: incrementa/decrementa X
        :y: incrementa/decrementa Y

        :returns: TRUE

        """
        x1,y1=self.posicion()
        self.mover(x1+x,y1+y)

        self._display.sync()
        print (x1+x,"--",y1+y)
        return True

    def posicion(self):
        """devuelve el valor de la posicion x,y del puntero del mouse
        :returns: (x,y)

        """
        coord = self._display.screen().root.query_pointer()._data
        return coord["root_x"], coord["root_y"]

    def click(self,boton):
        """ simula un click del mouse ('izquierdo', 'medio', 'derecho', 4, 5, 6, 7)
            :boton: el tipo de click del mouse.
        :returns: TRUE

        """
        cadena= "el argumento 'boton' no es igual a: ('izquierdo', 'medio', 'derecho', 4, 5, 6, 7)"
        assert boton in self.mapa_botones_mouse.keys(),cadena
        boton = self.mapa_botones_mouse[boton]
        fake_input(self._display, X.ButtonPress, boton)
        self._display.sync()
        fake_input(self._display, X.ButtonRelease, boton)
        self._display.sync()

    def tecla_press(self, key):
        """TODO: Docstring for tecla_press.

        :boton: TODO
        :returns: TODO

        """
        boton = self._display.keysym_to_keycode(Xlib.XK.string_to_keysym(str(key)))
        if boton == 0 :
            print ("el simbolo: ",boton," no es reconocido como un simbolo valido")
            return 0
        else:
            fake_input(self._display,X.KeyPress, boton)
            fake_input(self._display,X.KeyRelease, boton)
            self._display.sync()



