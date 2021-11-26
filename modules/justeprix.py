# Import method from module
from random import randint


def is_price(real_price, price):
    """
    --- Compares price given by the user and the real price generated
    :param real_price: Is the price generated
    :param price: Is the user price entrie
    :return: Success or not
    """
    if price > real_price:
        print("Fail, number is under. Try again")
        return False
    elif price < real_price:
        print("Fail, number is upper. Try again")
        return False
    else:
        print("Successful !!")
        return True


def win_or_loose(win, lose):
    """
    --- Define if the game.py is win or loose
    :param win: Take total wins
    :param lose: Take total losts
    :return: Victory or not
    """
    if win > lose:
        print("Game over, you won !!")
    else:
        print("Game over, you loose.")


def input_integer(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a number")


def correctprice():
    """
    --- Main programm
    :return:
    """
    turn = 3
    win = 0
    lost = 0

    while turn > 0:
        real_price = randint(1, 100)
        print("Welcome to the $$ Right Price $$. So, what's the price ? 1 to 100... Good luck")

        while True:

            price = input_integer("What's the real price ?")
            your_price = int(price)
            try_out = 7
            try_out = try_out - 1
            print("Remaining tries", try_out)

            while try_out > 0 & is_price(real_price, your_price):

                price = input_integer("What's the real price ?")
                your_price = int(price)

                if not is_price(real_price, your_price):
                    try_out = try_out - 1
                    print("Remaining tries", try_out)

                if try_out == 0:
                    print("Game over")
                    lost += 1
                    break

                if is_price(real_price, your_price):
                    win += 1
                    break

            turn = turn - 1
            print("Win : ", win, " - Loose : ", lost)
            break

    win_or_loose(win, lost)