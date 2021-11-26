def calculate(*args):
    total = [arg for arg in args if arg > 0]
    return sum(total)


def concat(**kwargs):
    concatenate = ""
    for value in kwargs:
        concatenate += value + " "
    return concatenate


def args_kwargs():
    print(calculate(1, 2, 3, 9, 100, 900, -1, -1000, 33))
    print(concat(toto=["toto"], titi=1, tete="Tete", tyty="TyTy"))

