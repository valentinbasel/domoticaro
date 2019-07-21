#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!3#!3

###############################################################################
#
# clase para manejo del chatbot TELEGRAM
# Copyright © 2019 Valentín Basel <valentinbasel@gmail.com>
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
#
###############################################################################

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

class CHATBOT(object):
    """Docstring for CHATBOT.

        Capas de abstracción para el manejo y creación de un bot conversacional
    """

    def __init__(self,token):
        """

        :token: TODO

        """
        self.update=None
        self.context=None
        self.updater = Updater(token , use_context=True)
        self.ordenes={}
        self.mensajes={}
        self.__mensaje_usuario=""
        self.__recibir=None

    def manejador_ordenes(self, update,context):
        """TODO: Docstring for manejador.

        :arg1: TODO
        :returns: TODO

        """
        self.update = update
        self.context = context
        key=str(update.message.text).strip("/")
        self.__mensaje_usuario = update.message.text
        a=self.ordenes[key]
        a()


    def manejador_mensajes(self, update,context):
        """TODO: Docstring for manejador.

        :arg1: TODO
        :returns: TODO

        """
        self.update = update
        self.context = context
        key=str(update.message.text)
        self.__mensaje_usuario = key
        self.__recibir()

    def mensaje_usuario (self):
        """TODO: Docstring for mensaje_usuario
        :returns: self.__mensaje_usuario

        """
        return self.__mensaje_usuario 

    def recibir(self, arg1):
        """TODO: Docstring for recibir.

        :arg1: TODO
        :returns: TODO

        """
        self.__recibir = arg1
    def mensaje(self,arg1):
        """TODO: Docstring for mensaje.

        :arg1: TODO
        :returns: TODO

        """
        self.update.message.reply_text(arg1)

    def _error(self,update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)
        print(context.error)

    def bucle_espera(self):
        """TODO: Docstring for bucle_espera.
        :returns: TODO

        """
        dp = self.updater.dispatcher
        for orden in self.ordenes.keys():
            dp.add_handler(CommandHandler(orden, self.manejador_ordenes))
        dp.add_handler(MessageHandler(Filters.text, self.manejador_mensajes))
        dp.add_error_handler(self._error)
        self.updater.start_polling()
        self.updater.idle()

