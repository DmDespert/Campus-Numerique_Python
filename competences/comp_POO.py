# Vous n'avez pas le droit de modifier la classe CalculSurListe
# Les classes CalculSurListeSomme et CalculSurListeProduit ne doivent pas avoir de méthode calculer
# CalculSurListeSomme doit calculer la somme des nombres
# CalculSurListeProduit doit calculer le produit des nombres

class CalculSurListe():
    def __init__(self, liste):
        self.__liste = liste

    def calculer(self):
        return self._calculer(self.__liste)

    def _calculer(self, liste):
        raise Exception("Not implemented")


class CalculSurListeSomme(CalculSurListe):
    def __init__(self, liste):
        super().__init__(liste)

    def _calculer(self, liste):
        return sum(liste)


class CalculSurListeProduit(CalculSurListe):
    def __init__(self, liste):
        super().__init__(liste)

    def _calculer(self, liste):
        y = liste[0]
        for i in liste:
            y = y * i
        return y


if __name__ == '__main__':
    # c = CalculSurListe([1, 2, 3, 4])
    c = CalculSurListeSomme([1, 2, 3, 4])
    print(c.calculer())
    c = CalculSurListeProduit([1, 2, 3, 4])
    print(c.calculer())
