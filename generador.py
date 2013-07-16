# -*- coding: utf-8 -*-
"""
Generador de palabras "pronunciables"

¿Cansado de las mismas palabras?
¡Genera las tuyas e inventa tu propio dialecto!
"""

import argparse
import random

CONSONANTES = ['b', 'br', 'bl',
    'c', 'cr', 'cl',
    'd', 'dr',
    'f', 'fr', 'fl',
    'g', 'gr', 'gl',
    'h', 'j', 'k', 'l', 'm', 'n',
    'p', 'pr', 'pl',
    'q', 'r', 's',
    't', 'tr', 'tl',
    'v', 'w', 'wr',
    'x', 'y', 'z']

VOCALES = ['a', 'ae', 'ai', 'ao', 'au',
    'e', 'ea', 'ee', 'ei', 'eo', 'eu',
    'i', 'ia', 'ie', 'io', 'iu',
    'o', 'oa', 'oe', 'oi', 'oo', 'ou',
    'u', 'ua', 'ue', 'ui', 'uo', 'uu',
    'y']


def rand(consonantes, vocales):
    'Combina una consonante y una vocal seleccionadas pseudoaleatoriamente'
    return random.choice(consonantes) + random.choice(vocales)


def palabra(longitud, consonantes, vocales):
    'Genera una nueva palabra'
    return ''.join(__genera(longitud, consonantes, vocales))


def __genera(longitud, consonantes, vocales):
    'Genera una lista de sílabas'
    for _ in range(longitud):
        yield rand(consonantes, vocales)


def main():
    'Punto inicial del programa'
    cuantas = int(raw_input('¿Cuántas palabras nuevas quieres generar? '))
    for _ in range(cuantas):
        print palabra(random.randrange(1, 6, 1), CONSONANTES, VOCALES)


if __name__ == '__main__':
    main()
