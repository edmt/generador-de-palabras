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


def genera_palabra(longitud, consonantes, vocales):
    'Genera una nueva palabra'
    return ''.join(genera_silaba(longitud, consonantes, vocales))


def genera_silaba(longitud, consonantes, vocales):
    'Genera una lista de sílabas'
    for _ in range(longitud):
        if random.random() > 0.5:
            yield random.choice(consonantes) + random.choice(vocales)
        else:
            yield random.choice(vocales) + random.choice(consonantes)


def main(args):
    'Punto inicial del programa'
    for _ in range(args.N):
        print genera_palabra(random.randrange(1, 5, 1), CONSONANTES, VOCALES)


if __name__ == '__main__':
    __argparser__ = argparse.ArgumentParser(description='XML eater')
    __argparser__.add_argument('N', type=int,
        help=u'Cantidad de palabras que se desea generar')
    main(__argparser__.parse_args())
