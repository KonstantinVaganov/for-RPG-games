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
    _armor = ''
    _weapon = ''
    _stats_character = {}
    _up_stats_character = []

    def __init__(self, name):
        self.name = name

    def mage(self):
        if self._character is None:
            self._armor = 'robe'
            self._weapon = 'Dragon mace'
            self._character = 'Маг'
            self._stats_character = {'speed': 19, 'caste_rate': 30, 'magic_attack': 260, 'health': 200}
            self._up_stats_character = ['magic_attack', 'health']
            print(f"\nВы выбрали играть за Мага. Ваш тип брони {self._armor}\n")
            print(f"Ваши статы {self._stats_character}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def warrior(self):
        if self._character is None:
            self._armor = 'heavy'
            self._weapon = 'Dragon sword'
            self._character = 'Воин'
            self._stats_character = {'speed': 18, 'attack_speed': 40, 'attack_power': 200, 'health': 380}
            self._up_stats_character = ['attack_power', 'health']
            print(f"\nВы выбрали играть за Воина. Ваш тип брони {self._armor}\n")
            print(f"Ваши статы {self._stats_character}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def hunter(self):
        if self._character is None:
            self._armor = 'leather'
            self._weapon = 'Dragon bow'
            self._character = 'Охотник'
            self._stats_character = {'speed': 22, 'attack_speed': 44, 'attack_power': 160, 'health': 230}
            self._up_stats_character = ['attack_power', 'health']
            print(f"\nВы выбрали играть за Охотника. Ваш тип брони {self._armor}\n")
            print(f"Ваши статы {self._stats_character}\n")
        else:
            print(f'Вы уже выбрали класс {self._character}a')


class Weapon(CharacterClass):

    def weapon_selection(self):
        print(f'Ваше оружие {self._weapon}, Оружие можно заточить, при каждой заточки статы увеличиваются. ')
        print('Шанс заточить оружие на +1 == 100%, на +2 шанс уже 95%.')
        print('С каждой заточкой шанс уменьшается на 5 % ')
        print('Максимальная заточка оружия +5')


class WeaponEnhancement(Weapon):
    _lvl_enhancement = 0
    _stats_none = {}

    def increase_lvl_weapon(self):
        if self._lvl_enhancement == 0:
            if choice_in_percent(100, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats_none = dict(self._stats_mage)
                    self._stats_mage['magic_attack'] += 30
                    print(f'Статы персонажа {self._stats_mage}')
                elif self._character == 'Воин':
                    self._stats_none = dict(self._stats_warrior)
                    self._stats_warrior['attack_power'] += 20
                    print(f'Статы персонажа {self._stats_warrior}')
                else:
                    self._stats_none = dict(self._stats_hunter)
                    self._stats_hunter['attack_power'] += 25
                    print(f'Статы персонажа {self._stats_hunter}')
        elif self._lvl_enhancement == 1:
            if choice_in_percent(95, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats_mage['magic_attack'] += 30
                    print(f'Статы персонажа {self._stats_mage}')
                elif self._character == 'Воин':
                    self._stats_warrior['attack_power'] += 20
                    print(f'Статы персонажа {self._stats_warrior}')
                else:
                    self._stats_hunter['attack_power'] += 25
                    print(f'Статы персонажа {self._stats_hunter}')
            else:
                if self._character == 'Маг':
                    self._stats_mage = dict(self._stats_none)
                elif self._character == 'Воин':
                    self._stats_warrior = dict(self._stats_none)
                else:
                    self._stats_hunter = dict(self._stats_none)
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 2:
            if choice_in_percent(90, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats_mage['magic_attack'] += 30
                    print(f'Статы персонажа {self._stats_mage}')
                elif self._character == 'Воин':
                    self._stats_warrior['attack_power'] += 20
                    print(f'Статы персонажа {self._stats_warrior}')
                else:
                    self._stats_hunter['attack_power'] += 25
                    print(f'Статы персонажа {self._stats_hunter}')
            else:
                if self._character == 'Маг':
                    self._stats_mage = dict(self._stats_none)
                elif self._character == 'Воин':
                    self._stats_warrior = dict(self._stats_none)
                else:
                    self._stats_hunter = dict(self._stats_none)
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 3:
            if choice_in_percent(85, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats_mage['magic_attack'] += 30
                    print(f'Статы персонажа {self._stats_mage}')
                elif self._character == 'Воин':
                    self._stats_warrior['attack_power'] += 20
                    print(f'Статы персонажа {self._stats_warrior}')
                else:
                    self._stats_hunter['attack_power'] += 25
                    print(f'Статы персонажа {self._stats_hunter}')
            else:
                if self._character == 'Маг':
                    self._stats_mage = dict(self._stats_none)
                elif self._character == 'Воин':
                    self._stats_warrior = dict(self._stats_none)
                else:
                    self._stats_hunter = dict(self._stats_none)
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        elif self._lvl_enhancement == 4:
            if choice_in_percent(80, 'Удачно', 'Неудачно') == 'Удачно':
                self._lvl_enhancement += 1
                print(f'\n{self._weapon} +{self._lvl_enhancement}')
                if self._character == 'Маг':
                    self._stats_mage['magic_attack'] += 30
                    print(f'Статы персонажа {self._stats_mage}')
                elif self._character == 'Воин':
                    self._stats_warrior['attack_power'] += 20
                    print(f'Статы персонажа {self._stats_warrior}')
                else:
                    self._stats_hunter['attack_power'] += 25
                    print(f'Статы персонажа {self._stats_hunter}')
            else:
                if self._character == 'Маг':
                    self._stats_mage = dict(self._stats_none)
                elif self._character == 'Воин':
                    self._stats_warrior = dict(self._stats_none)
                else:
                    self._stats_hunter = dict(self._stats_none)
                self._lvl_enhancement = 0
                print(f'К сожилению заточка не удалась, уровень заточки спадает до {self._lvl_enhancement}')
        else:
            print(f'Достигнута максимальная заточка оружия +{self._lvl_enhancement}')


p1 = WeaponEnhancement('Player')
p1.hunter()
p1.weapon_selection()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
p1.increase_lvl_weapon()
