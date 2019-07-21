#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#
# -roboticaro-
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
###############################################################################

from .opencv.camara import CAM
from .xlib_notebook.interface_falsa import INTERFACES
from .voz.espeak import VOZ

class ROBOT(object):

    """Docstring for RobotIcaro. """

    def __init__(self,placa):
        """TODO: to be defined1. """
        self.camara = CAM()
        self.voz = VOZ()
        self.interfaces=INTERFACES()
        if placa == "icaro_cdc":
            from .hardware.icaro import PIC18F4550
            self.hardware=PIC18F4550("cdc")


def iniciar(placa = "icaro_cdc"):
    """TODO: Docstring for iniciar.
    :returns: TODO

    """
    placas=["icaro_cdc"]
    if placa in placas:
        robot=ROBOT(placa)
    else:
        print("la variable :",placa, " no es un valor reconocido")
        print ("se inicia el hardware con el emulador")
        robot = ROBOT("emulador")
    return robot
