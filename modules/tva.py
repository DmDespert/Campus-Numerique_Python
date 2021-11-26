# Programme calcule périmètre d'un cercle
# Rayon demandé au clavier

import math


def calc_ttc(prix, taxe):
    """
    :param prix: Prix du produit
    :param taxe: Taxe du produit
    :return: TTC Produit
    """
    taxe = prix * taxe / 100
    total = prix + taxe
    return total


def remise_stock(total):
    """
    :param total: TTC Produit
    :return: Remise
    """
    remise = total * 12 / 100
    return remise


def totalttc():
    """
    Programme principal
    :return:
    """
    nom_produit = input("Nom du produit : ")
    while True:
        try:
            prix_produit = input("Prix du produit : ")
            prix = float(prix_produit)
            taxe_produit = input("Taxe du produit : ")
            taxe = math.ceil(float(taxe_produit))
            nb_stock = input("Stock du produit : ")
            stock = int(nb_stock)

            total = calc_ttc(prix, taxe)
            print("Le prix total TTC du produit est de", total)

            if stock * prix > 1000:
                remise = remise_stock(total)
                print("Le total du stock de", nom_produit, "est de", stock * prix, "(dont taxe de", taxe,
                      ") - remise de",
                      total - remise)
            else:
                print("Le total du stock de", nom_produit, "est de", stock * prix, "(dont taxe de", taxe, ").")

            break

        except ValueError:
            return ValueError