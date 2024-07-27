class CharacterClass:
    _character = None
    _stats = {}
    _armor = ''

    def __init__(self, name):
        self.name = name

    def mage(self):
        if self._character is None:
            self._armor = 'robe'
            print(f"\nВы выбрали играть за Мага. Ваш тип брони {self._armor}\n")
            self._character = 'Маг'
            self._stats.update(speed=19, caste_rate=30, magic_attack=260, health=200)
            print(f"Ваши статы {self._stats}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def warrior(self):
        if self._character is None:
            self._armor = 'heavy'
            print(f"\nВы выбрали играть за Воина. Ваш тип брони {self._armor}\n")
            self._character = 'Воин'
            self._stats.update(speed=18, attack_speed=40, attack_power=200, health=380)
            print(f"Ваши статы {self._stats}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def hunter(self):
        if self._character is None:
            self._armor = 'leather'
            print(f"\nВы выбрали играть за Охотника. Ваш тип брони {self._armor}\n")
            self._character = 'Охотник'
            self._stats.update(speed=22, attack_speed=44, attack_power=160, health=230)
            print(f"Ваши статы {self._stats}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')


class Weapon(CharacterClass):
    _weapon = ''

    def weapon_selection(self):
        if self._character == 'Маг':
            self._weapon = 'Dragon mace'
            print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
            print('Шанс заточить оружие на +1 == 100%, на +2 шанс уже 95%.')
            print('С каждой заточкой шанс уменьшается на 5 % ')
            print('Максимальная заточка оружия +10')
        elif self._character == 'Воин':
            self._weapon = 'Dragon sword'
            print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
            print('Шанс заточить оружие на +1 == 100%, на +2 шанс уже 95%.')
            print('С каждой заточкой шанс уменьшается на 5 % ')
            print('Максимальная заточка оружия +10')
        elif self._character == 'Охотник':
            self._weapon = 'Dragon bow'
            print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
            print('Шанс заточить оружие на +1 = 100%, на +2 шанс уже 95%.')
            print('С каждой заточкой шанс уменьшается на 5 % ')
            print('Максимальная заточка оружия +10')
        else:
            print("Сначало нужно выбрать класс за кого хотите играть")

class WeaponEnhancement(Weapon):
    pass


p1 = Weapon('Sledov')
p1.mage()
p1.weapon_selection()