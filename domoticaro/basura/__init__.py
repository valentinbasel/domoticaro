#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from opencv.camara import CAM
from xlib_notebook.interface_falsa import MOUSE
from hardware.apicaro import puerto
class ROBOT(object):

    """Docstring for RobotIcaro. """

    def __init__(self):
        """TODO: to be defined1. """
        self.camara=CAM()
        self.mouse=MOUSE()
        self.icaro=puerto()
def iniciar():
    """TODO: Docstring for iniciar.
    :returns: TODO

    """
    robot=ROBOT()
    return robot
