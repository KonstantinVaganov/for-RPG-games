class CharacterClass:
    _character = None
    _stats = {}
    _armor = ''

    def __init__(self, name):
        self.name = name

    def mage(self):
        if self._character is None:
            self._armor = 'robe'
            print(f"Вы выбрали играть за Мага. Ваш тип брони {self._armor}")
            self._character = 'Маг'
            self._stats.update(speed=19, caste_rate=30, magic_attack=260, health=200)
            print(f"Ваши статы {self._stats}")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def warrior(self):
        if self._character is None:
            self._armor = 'heavy'
            print(f"Вы выбрали играть за Воина. Ваш тип брони {self._armor}")
            self._character = 'Воин'
            self._stats.update(speed=18, attack_speed=40, attack_power=200, health=380)
            print(f"Ваши статы {self._stats}")
        else:
            print(f'Вы уже выбрали класс {self._character}a')

    def hunter(self):
        if self._character is None:
            self._armor = 'leather'
            print(f"Вы выбрали играть за Охотника. Ваш тип брони {self._armor}")
            self._character = 'Охотник'
            self._stats.update(speed=22, attack_speed=44, attack_power=160, health=230)
            print(f"Ваши статы {self._stats}")
        else:
            print(f'Вы уже выбрали класс {self._character}a')


p1 = CharacterClass('Sledov')
p1.warrior()
p1.hunter()

