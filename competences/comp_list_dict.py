# L'existence d'un élément d'une liste est vérifiée (in)

def tests():
    # Une liste est instanciée
    liststr = ['hello', 'world', 'i\'m', 'a', 'surgeon', 'world']
    listint = [1, 5, 120, 4]

    # Des éléments sont ajoutés à une liste (append)
    liststr.append('toto')
    print("Added 'toto' in ", liststr)

    # L'existence d'un élément d'une liste est vérifiée (in)
    print("Element 'toto' is inside ?", 'toto' in liststr)

    # Des éléments sont retirés d'une liste (del)
    # liststr.remove('world')
    del liststr[1]
    print("Deleted 'world' in", liststr)

    # Un élément est inséré dans une liste (insert)
    liststr.insert(1, "tata")
    print("Inserted 'tata' in list :", liststr)

    # Un élément est extrait d'une liste (pop)
    poped = liststr.pop(1)
    print("Poped item :", poped)

    # Deux listes sont fusionnées (extend)
    liststr.extend(listint)
    print("Extended :", liststr)

    # Un élément d'une liste précis est affecté à une variable ([n])
    myItem = liststr[1]
    print("My var got :", myItem)

    # Une liste d'entiers est triée
    # .sort(reverse)
    listint.sort()
    print("Sorted int list :", listint)

    # Une sous liste est créée à partir d'une liste (slice)
    print("Sliced elements : ", liststr[2:4])

    # Une liste est créée par copie d'une autre liste
    new_list = liststr.copy()
    print("Copied list :", new_list)

    # Deux variables font référence à une même liste, la liste est modifié à travers la première variable,
    # et le résultat est affiché à travers la deuxième variable
    myVar1 = liststr
    myVar2 = myVar1

    print("My var 1: ", myVar1)
    myVar1[2] = "Modify"
    print("My var 2 : ", myVar2)

    # La liste est affichée à l'écran au moyen d'une boucle for --
    y = ""
    for x in liststr:
        y += str(x)
    print("Concat liststr :", y)

    # Un dictionnaire est instancié / Un nouveau couple clé/valeur est ajouté au dictionnaire
    myDict = {1: "toto", 2: "tata", 3: "tete", 4: "tutu"}

    # Une valeur de la liste est affichée à partir de la clé (l[key]) -
    print("Show key[2] :", myDict[2])

    # Une valeur du dictionnaire est modifiée à partir de la clé
    myDict[2] = "titi"
    print("Modify 'tata' in", myDict)

    # Une clé du dictionnaire est supprimée (del)
    del myDict[1]
    print("Deleted 'toto' in", myDict)

    # L'existence d'une clé du dictionnaire est vérifiée (in)
    print("Element 'toto' is inside ?", 'toto' in myDict)

    # Le dictionnaire est affiché au moyen d'une boucle (clé et valeur)
    y = [key for key, value in myDict.items()]
    print("My dict keys & values", y)


def list_dict():
    tests()
    print("End.")
