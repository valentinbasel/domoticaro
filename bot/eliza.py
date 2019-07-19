#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# clase para implementación de ELIZA
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
import re
import random

class ELIZA(object):
    """ Class doc """
    

    # reflejos sobre el sujeto
    reflections = {
        "estoy": "estas",
        "soy": "eres",
        "fui": "fuiste",
        "yo": "tu",
        "deberia": "deberias",
        "tengo": "tendriass",
        "quiero": "quieres",
        "mio": "tuyo",
        "eres": "soy",
        "tu tienes": "yo tengo",
        "tu seras": "yo sere",
        "tuyo": "mio",
        "vuestro": "nuestro",
        "sobre ti": "sobre mi",
        "sobre mi": "sobre ti",
        "tu":"mi",
        "vos":"yo",

    }

    # patrones psicologicos más probables
    psychobabble = [
        [r'necesito(.*)',
         ["¿Por qué necesitas {0}?",
          "¿Realmente te ayudaría a obtener {0}?",
          "¿Está seguro de que necesitas {0}?"]],

        [r'por que no puedes ([^\?]*)\??' or r'por qué no puedes ([^\?]*)\??',
         ["¿De verdad crees que no lo hago? {0}?",
          "Tal vez eventualmente lo haré. {0}.",
          "¿De verdad quieres que yo {0}?"]],

        [r'¿Por que no puedo ([^\?]*)\??' or r'por que no puedo ([^\?]*)\??' or r'¿Por qué no puedo ([^\?]*)\??' or r'Por qué no puedo ([^\?]*)\??',
         ["¿Crees que deberías ser capaz de {0}?",
          "Si pudieras {0}, ¿qué harías?",
          "No sé - ¿por qué no puedes {0}?",
          "¿Lo has intentado realmente?",
          "Si no eres capaz de {0} entonces eso te define cómo un autentico marica!"]],

        [r'no puedo(.*)',
         ["¿Cómo sabes que no puedes{0}?",
          "Tal vez podría {0} si lo intentó.",
          "¿Qué se necesita para que usted {0}?"]],

        [r'yo soy (.*)',
         ["¿Has venido a mí porque eres  {0}?",
          "¿Cuánto tiempo has estado {0}?",
          "¿Cómo te sientes acerca de ser {0}?"]],

        [r'estoy (.*)',
         ["¿Cómo te hace sentir{0}?",
          "¿Te gusta ser {0}?",
          "¿Por qué me dices que eres{0}?",
          "¿Por qué crees que eres  {0}?"]],

        [r'¿ ([^\?]*)\??',
         ["¿Por qué importa si soy {0}?",
          "¿Lo preferirías si no fuera {0}?",
          "Tal vez usted piensa que soy.",
          "Puedo ser {0} - ¿qué piensas?"]],

        [r'¿qué (.*)' or r'qué (.*)' or r'que (.*)',
         ["¿Por qué preguntas?",
          "¿Cómo le ayudaría una respuesta a eso?",
          "¿Qué piensas?"]],

        [r'¿cómo (.*)' or r'cómo (.*)' or r'como (.*)',
         ["¿Cómo se supone?",
          "Tal vez puedas responder a tu propia pregunta.",
          "¿Qué estás realmente pidiendo?"]],

        [r'porque (.*)',
         ["¿Es esa la verdadera razón?",
          "¿Qué otras razones vienen a la mente?",
          "¿Esa razón se aplica a cualquier otra cosa?",
          "Si {0}, ¿qué otra cosa debe ser verdadera?"]],

        [r'(.*) lo siento (.*)',
         ["Hay muchas veces cuando no se necesita disculpa.",
          "¿Qué sentimientos tiene cuando se disculpa?"]],

        [r'hola(.*)',
         ["Hola ... me alegro de que puedas pasar por hoy.",
          "¿Hola, cómo estas hoy?",
          "Hola, ¿cómo te sientes hoy?"]],

        [r'pienso (.*)',
         ["¿Dudas {0}?",
          "¿De verdad piensas eso?",
          "Pero no estás seguro {0}?"]],

        [r'(.*) amigo (.*)',
         ["Cuéntame más sobre tus amigos.",
          "Cuando piensas en un amigo, ¿qué te viene a la mente?",
          "¿Por qué no me hablas de un amigo desde la infancia?"]],

        [r'si',
         ["Pareces muy seguro.",
          "Está bien, pero ¿puedes hacer algo?"]],

        [r'(.*) ordenador(.*)',
         ["¿De verdad estás hablando de mí?",
          "¿Parece extraño hablar con una computadora?",
          "¿Cómo te hacen sentir las computadoras?",
          "¿Se siente amenazado por las computadoras?"]],

        [r'eso es (.*)',
         ["¿Crees que es {0}?",
          "Tal vez sea {0} - ¿qué piensas?",
          "Si fuera {0}, ¿qué harías?",
          "Podría ser que {0}."]],

        [r'es eso (.*)',
         ["Pareces muy seguro.",
          "Si te dijera que probablemente no es {0}, ¿qué sentirías?"]],

        [r'¿puedes ([^\?]*)\??',
         ["¿Qué te hace pensar que no puedo {0}?",
          "Si pudiera {0}, ¿entonces qué?",
          "¿Por qué me preguntas si puedo (0)?"]],

        [r'puedo ([^\?]*)\??',
         ["No puedes querer {0}.",
          "¿Quieres ser capaz de {0}?",
          "Si pudieras {0}, ¿cierto?"]],

        [r'tu eres (.*)' or r'¿tu eres (.*)',
         ["¿Por qué crees que soy {0}?",
          "¿Te gusta pensar que soy {0}?",
          "Tal vez usted quiere que sea.",
          "¿Tal vez estás hablando de ti?"]],

        [r'¿eres ture (.*)',
         ["¿Por qué dices que soy {0}?",
          "¿Por qué crees que soy {0}?",
          "¿Estamos hablando de ti o de mí?"]],

        [r'¿no lo hago (.*)',
         ["No realmente {0}?",
          "¿Por qué no {0}?",
          "¿Quieres {0}?"]],

        [r'me siento (.*)',
         ["Bueno, cuéntame más sobre estos sentimientos.",
          "¿Sientes a menudo {0}?",
          "¿Cuándo sientes normalmente {0}?",
          "Cuando sientes {0}, ¿qué haces?"]],

        [r'yo tengo (.*)',
         ["¿Por qué me dices que tienes {0}?",
          "¿Realmente tienes {0}?",
          "Ahora que tienes {0}, ¿qué harás después?"]],

        [r'yo debo (.*)',
         ["¿Podría explicar por qué lo haría?",
          "¿Por que lo harias?",
          "¿Quién más sabe que lo harías?"]],

        [r'esta ahí (.*)',
         ["¿Crees que hay {0}?",
          "Es probable que haya {0}.",
          "¿Te gustaría tener {0}?"]],

        [r'mi (.*)',
         ["Ya veo, tu {0}.",
          "¿Por qué dices que tu {0}?",
          "Cuando tu {0}, ¿cómo te sientes?"]],

        [r'tu (.*)',
         ["debemos estar discutiendo contigo, no conmigo.",
          "¿Por qué dices eso de mí?",
          "¿Por qué te importa si yo {0}?"]],

        [r'por qué (.*)',
         ["¿Por qué no me dices la razón por la cual {0}?",
          "¿Por qué crees que {0}?"]],

        [r'quiero que (.*)',
         ["¿Qué significaría para ti si tienes {0}?",
          "¿Por qué quieres {0}?",
          "¿Qué harías si tuvieras {0}?",
          "Si tienes {0}, entonces ¿qué harías?"]],

        [r'(.*) madre(.*)',
         ["Cuéntame más sobre tu madre.",
          "¿Cómo era tu relación con tu madre?",
          "¿Cómo te sientes con tu madre?",
          "¿Cómo se relaciona esto con tus sentimientos hoy?",
          "Las buenas relaciones familiares son importantes."]],

        [r'(.*) padre(.*)',
         ["Cuéntame más sobre tu padre.",
          "¿Cómo te hizo sentir tu padre?",
          "¿Cómo te sientes con tu padre?",
          "¿Su relación con su padre se relaciona con sus sentimientos hoy?",
          "¿Tiene problemas para mostrar afecto con su familia?"]],

        [r'(.*) niño(.*)',
         ["¿Tenías amigos íntimos cuando era niño?",
          "¿Cuál es tu recuerdo favorito de la niñez?",
          "¿Recuerdas algún sueño o pesadilla desde la infancia?",
          "¿Alguna vez te han molestado los otros niños?",
          "¿Cómo crees que tus experiencias infantiles se relacionan con tus sentimientos hoy?"]],

        [r'(.*)\?',
         ["¿Porque preguntas eso?",
          "Por favor, considere si puede responder a su propia pregunta.",
          "¿Quizás la respuesta está dentro de ti?",
          "¿Por qué no me lo dices?"]],

        [r'adios',
         ["Gracias por hablar conmigo.",
          "Adiós.",
          "Gracias, eso será $ 150. ¡Que tengas un buen día!"]],

        [r'(.*)',
         ["Por favor, cuéntame más.",
          "Vamos a cambiar de enfoque un poco ... Háblame de tu familia.",
          "¿Puedes profundizar sobre eso?",
          "¿Por qué dices eso {0}?",
          "Ya veo.",
          "Muy interesante.",
          "{0}.",
          "Ya veo, ¿y qué te dice eso?",
          "¿Cómo te hace sentir eso?",
          "¿Cómo te sientes cuando dices eso?"]]
    ]

    def __init__ (self):
        """ Class initialiser """
        pass

    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reflections:
                tokens[i] = self.reflections[token]
        return ' '.join(tokens)


    def analyze(self,statement):
        for pattern, responses in self.psychobabble:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response.format(*[self.reflect(g) for g in match.groups()])

