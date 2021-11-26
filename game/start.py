import random
import time
import colorama
from colorama import Fore

from allclass.charclass import Warrior
from allclass.charclass import Wizard
from allclass.charclass import Rogue

from utils.utils import input_integer


def generate_player():
    choice = input_integer(Fore.MAGENTA + "Choose a char : 1) Warrior / 2) Wizard / 3) Rogue : ")
    if choice == 1:
        return Warrior()
    if choice == 2:
        return Wizard()
    if choice == 3:
        return Rogue()


def generate_enemy():
    rand = random.randint(1, 3)
    if rand == 1:
        return Warrior()
    if rand == 2:
        return Wizard()
    if rand == 3:
        return Rogue()


def game_running(enemy, player, level):
    while enemy.get_life() > 0 and player.get_life() > 0:
        if enemy.__class__ == Warrior or enemy.__class__ == Rogue:
            before = player.get_life()
            player.set_life(player.get_life() - (enemy.phy_attack() - player.phy_defense()))
            print(Fore.RED + "You take :", before - player.get_life(), Fore.CYAN + "- remaining :", player.get_life(),
                  "HP")
        if enemy.__class__ == Wizard:
            before = player.get_life()
            player.set_life(player.get_life() - (enemy.mag_attack() - player.mag_defense()))
            print(Fore.RED + "You take :", before - player.get_life(), Fore.CYAN + "- remaining :", player.get_life(),
                  "HP")
        if player.get_life() < 0:
            print(Fore.RED + "You died X.X")
            break

        time.sleep(2)

        if player.__class__ == Warrior or player.__class__ == Rogue:
            before = enemy.get_life()
            enemy.set_life(enemy.get_life() - (player.phy_attack() - enemy.phy_defense()))
            print(Fore.GREEN + "You hit for :", before - enemy.get_life())
        if player.__class__ == Wizard:
            before = enemy.get_life()
            enemy.set_life(enemy.get_life() - (player.mag_attack() - enemy.mag_defense()))
            print(Fore.GREEN + "You hit for :", before - enemy.get_life())

        print(Fore.YELLOW + ">> Enemy life :", enemy.get_life())

        if enemy.get_life() < 0:
            print(Fore.YELLOW + "Enemy died")
            player.set_life(player.get_life() + 50)
            level += 1
            print(Fore.GREEN + "LEVEL UP ! Level is now", level, ". HP +50")
            break


def new_game():
    choice = input_integer(Fore.MAGENTA + "New game ? 1) Yes / 2) No : ")
    if choice == 1:
        gameload()
    else:
        exit()


def gameload():

    # -- Introduction
    print(Fore.CYAN + "Lllllleeeet's get ready to RUMMMMMBLLLEEEE !!!")
    time.sleep(2)
    print(Fore.CYAN + "Introduice music : Tintintin tin tin tintintin tin tin tin tinnnnnnn")
    time.sleep(2)
    print(Fore.CYAN + "TIINNNNN TIN TIN NNNNN....")
    time.sleep(2)
    print(Fore.CYAN + "TINTINTIN TIN TIN TINTINTIN TIN TIN TIN NNNNNNNNNN....")
    time.sleep(2)
    print(Fore.CYAN + "NNNNnnnn tin tin....")
    time.sleep(6)
    print(Fore.CYAN + "Hum, hm. Sorry...")
    time.sleep(1)

    # -- Generate new player - choose
    player = generate_player()
    level = 1

    print(Fore.CYAN + "Ready player ?")
    time.sleep(3)

    while player.get_life() > 0:

        # -- Generate new enemy till death !!
        enemy = generate_enemy()

        print(Fore.CYAN + "Enemy is a", enemy.get_class())

        # -- Game running
        game_running(enemy, player, level)

    print(Fore.CYAN + "Game over")

    # -- End, new game ?
    new_game()


if __name__ == "__main__":
    gameload()
