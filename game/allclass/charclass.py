from random import randint


class Char:
    def __init__(self):
        self.__life = 200

    def phy_attack(self):
        return self._phy_attack()

    def phy_defense(self):
        return self._phy_defense()

    def mag_attack(self):
        return self._mag_attack()

    def mag_defense(self):
        return self._mag_defense()

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def _phy_attack(self):
        return randint(10, 20)

    def _phy_defense(self):
        return randint(5, 15)

    def _mag_attack(self):
        return randint(10, 20)

    def _mag_defense(self):
        return randint(5, 15)


class Warrior(Char):
    def __init__(self):
        super(Warrior, self).__init__()
        self.__classname = "Warrior"

    def _phy_attack(self):
        return int(super()._phy_attack() * 2)

    def _phy_defense(self):
        return int(super()._phy_defense() * 1.2)

    def _mag_defense(self):
        return int(super()._mag_defense() * 0.7)

    def get_class(self):
        return self.__classname


class Wizard(Char):
    def __init__(self):
        super(Wizard, self).__init__()
        self.set_life(self.get_life() * 0.8)
        self.__classname = "Wizard"

    def _mag_attack(self):
        return int(super()._mag_attack() * 3)

    def _phy_defense(self):
        return int(super()._phy_defense() * 0.7)

    def _mag_defense(self):
        return int(super()._mag_defense() * 1.2)

    def get_class(self):
        return self.__classname


class Rogue(Char):
    def __init__(self):
        super(Rogue, self).__init__()
        self.set_life(self.get_life() * 1.2)
        self.__classname = "Rogue"

    def _phy_attack(self):
        return int(super()._phy_attack() * 1.4)

    def _phy_defense(self):
        return int(super()._phy_defense() * 0.8)

    def _mag_defense(self):
        return int(super()._mag_defense() * 0.8)

    def get_class(self):
        return self.__classname
