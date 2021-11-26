# Programme calcule périmètre d'un cercle
# Rayon demandé au clavier

import math


def perimetre_cercle(rayon):
    """
    :param rayon: rayon du cercle
    :return: périmètre d'un cercle
    """
    diametre = 2 * rayon
    return math.pi * diametre


def circle():
    """
    Programme principal
    :return:
    """
    saisie = input("Rayon du cercle : ")
    rayon = float(saisie)

    perimetre = perimetre_cercle(rayon)

    print("Le périmètre d'un cercle de rayon ", rayon, " est ", perimetre)

