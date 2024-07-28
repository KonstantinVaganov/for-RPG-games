import random


def choice_in_percent(percent, arg1, arg2):
    ''' Для работы нужно импортировать модуль random.
        percent = указать проценты
        arg1 = с шансом (percent) выпадет arg1
        arg2 = с шансом (100 - percent) выпадет arg2 '''
    full = 100
    result = []
    full -= percent
    for i in range(full):
        result.append(arg2)
    for j in range(percent):
        result.append(arg1)
    return random.choice(result)


class CharacterClass:
    _character = None
    _stats = {}
    _stats_copy = _stats.copy()
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
            print('Максимальная заточка оружия +5')
        elif self._character == 'Воин':
            self._weapon = 'Dragon sword'
            print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
            print('Шанс заточить оружие на +1 == 100%, на +2 шанс уже 95%.')
            print('С каждой заточкой шанс уменьшается на 5 % ')
            print('Максимальная заточка оружия +5')
        elif self._character == 'Охотник':
            self._weapon = 'Dragon bow'
            print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
            print('Шанс заточить оружие на +1 = 100%, на +2 шанс уже 95%.')
            print('С каждой заточкой шанс уменьшается на 5 % ')
            print('Максимальная заточка оружия +5')
        else:
            print("Сначало нужно выбрать класс за кого хотите играть")


class WeaponEnhancement(Weapon):
    _lvl_enhancement = 0


    def increase_lvl_weapon(self):
        if self._lvl_enhancement == 0:
            if choice_in_percent(100, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats['magic_attack'] += 25
                else:
                    self._stats['attack_power'] += 20
                print(f'Статы персонажа {self._stats}')
        elif self._lvl_enhancement == 1:
            if choice_in_percent(95, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats['magic_attack'] += 25
                else:
                    self._stats['attack_power'] += 20
                print(f'Статы персонажа {self._stats}')
            else:
                self._stats = self._stats_copy.copy()
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 2:
            if choice_in_percent(90, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats['magic_attack'] += 25
                else:
                    self._stats['attack_power'] += 20
                print(f'Статы персонажа {self._stats}')
            else:
                self._stats = self._stats_copy.copy()
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 3:
            if choice_in_percent(85, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats['magic_attack'] += 25
                else:
                    self._stats['attack_power'] += 20
                print(f'Статы персонажа {self._stats}')
            else:
                self._stats = self._stats_copy.copy()
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 4:
            if choice_in_percent(80, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats['magic_attack'] += 25
                else:
                    self._stats['attack_power'] += 20
                print(f'Статы персонажа {self._stats}')
            else:
                self._stats = self._stats_copy.copy()
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        else:
            print(f'Достигнута максимальная заточка оружия +{self._lvl_enhancement}')


p1 = WeaponEnhancement('Player')
p1.mage()
p1.weapon_selection()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
