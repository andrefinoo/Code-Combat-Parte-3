import random

class Icebreaker:

    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.__name = name
        self.__min_damage = 1
        self.__max_damage = 1
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.__type = "decoder"
        self.type = type

    @property
    def name(self):
        return self.__name

    @property
    def min_damage(self):
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, value: int):
        if not isinstance(value, int):
            value = 1

        if value < 1:
            value = 1

        if value > self.__max_damage:
             self.__max_damage = value

        self.__min_damage = value

    @property
    def max_damage(self):
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value: int):
        if not isinstance(value, int):
            value = self.__min_damage

        if value < self.__min_damage:
            value = self.__min_damage

        self.__max_damage = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value: str):
        if value in {"fracter", "decoder"}:
            self.__type = value
        else:
            self.__type = "decoder"

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"{self.__name} {self.__type.capitalize()} ({self.__min_damage}-{self.__max_damage} dmg)"