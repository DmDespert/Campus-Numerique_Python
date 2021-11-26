def entry(text):
    msg = "Nope, only number > 0"
    while True:
        try:
            user_entry = int(input(text))
            if user_entry > 0:
                return user_entry
            else:
                print(msg)
        except ValueError:
            print(msg)


def calculate(entry1, entry2, entry3):
    return entry1 + entry2 + entry3


def entries():
    try:
        first = entry("1) Entier 1 : ")
        second = entry("2) Entier 2 : ")
        third = entry("3) Entier 3 : ")
        return print(calculate(first, second, third))
    except ValueError:
        print(ValueError)

