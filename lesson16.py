# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100).
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Только маг может увеличить интелект на 1 пункт, максимум 10.
# Только лучник может увеличить ловкость на 1 пункт, максимум 10.
# Только рыцарь может увеличить силу на 1 пункт, максимум 10.

class Unit:
    def __init__(self, name, clan):
        self._name = name
        self._clan = clan
        self._health = 100
        self._strenght = 1
        self._agility = 1
        self._intellect = 1
        # self._additional_skill = ''

    def increase_health(self):
        if self._health <= 90:
            self._health += 10
        else:
            self._health = 100

    def increase_base_skill(self):
        raise Exception("Must be implement in child class")

    def __repr__(self):
        return f"Name: {self._name}\nClan: {self._clan}\nHealth: {self._health}\n" \
               f"Strenght: {self._strenght}\nAgility: {self._agility}\nIntellect: {self._intellect}"

    # def __repr__(self):
    #     return f"Name: {self._name}\nClan: {self._clan}\nHealth: {self._health}\n" \
    #            f"Strenght: {self._strenght}\nAgility: {self._agility}\nIntellect: {self._intellect}\n" \
    #            f"{type(self).__name__} skill: {self._additional_skill}"

class Magic(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)
        self._additional_skill = type_magic

    def increase_base_skill(self):
        if self._intellect <= 9:
            self._intellect += 1
        else:
            self._intellect = 10

    def __repr__(self):
        return super().__repr__() + f"\nMagic type: {self._additional_skill}"

    # def __repr__(self):
    #     return super().__repr__(f"\nMagic type: {self._additional_skill}")


mage = Magic("Gendalf", "Humans", "Fire")

print(mage)
print('----------------------')
mage.increase_base_skill()
print(mage)


# def checkio(expression):
#     stack = []
#     braces = {")":"(", "]":"[", "}":"{"}
#     for symbol in expression:
#         if symbol in braces.values():
#             stack.append(symbol)
#         elif symbol in braces:
#             if len(stack) == 0:
#                 return False
#             elif stack[-1] == braces[symbol]:
#                 stack.pop()
#             elif stack[-1] != braces[symbol]:
#                 return False
#     return len(stack) == 0