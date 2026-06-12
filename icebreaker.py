import random

class Icebreaker:

    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.__name = name
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__type = type

        if not isinstance(self.__min_damage, int):
            print("Attenzione: min_damage deve essere un intero. Corretto a 1.")
            self.__min_damage = 1
        elif self.__min_damage < 1:
            print("Attenzione: min_damage deve essere >= 1. Corretto a 1.")
            self.__min_damage = 1

        if not isinstance(self.__max_damage, int):
            print("Attenzione: max_damage deve essere un intero. Corretto a min_damage.")
            self.__max_damage = self.__min_damage
        elif self.__max_damage < self.__min_damage:
            print("Attenzione: max_damage deve essere >= min_damage. Corretto.")
            self.__max_damage = self.__min_damage

        if type != "fracter" and type != "decoder":
            print("Attenzione: type deve essere 'fracter' o 'decoder'. Corretto a 'decoder'.")
            self.__type = "decoder"

    def get_name(self) -> str:
        return self.__name

    def get_min_damage(self):
        return self.__min_damage

    def get_max_damage(self):
        return self.__max_damage

    def get_type(self):
        return self.__type

    def set_min_damage(self, value: int):
        if not isinstance(value, int):
            print("Attenzione: min_damage deve essere un intero.")
            return
        elif value < 1:
            print("Attenzione: min_damage deve essere >= 1.")
            return
        elif value > self.__max_damage:
            print("Attenzione: min_damage non può essere maggiore di max_damage.")
            return

        self.__min_damage = value

    def set_max_damage(self, value: int):
        if not isinstance(value, int):
            print("Attenzione: max_damage deve essere un intero.")
            return
        elif value < 1:
            print("Attenzione: max_damage deve essere >= 1.")
            return
        elif value < self.__min_damage:
            print("Attenzione: max_damage non può essere minore di min_damage.")
            return

        self.__max_damage = value

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"{self.__name} {self.__type.capitalize()} ({self.__min_damage}–{self.__max_damage} dmg)"