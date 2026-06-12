from icebreaker import Icebreaker


class Runner:

    def __init__(self, handle: str, max_integrity: int, power: int, finesse: int):
        self.__handle = handle
        self.__max_integrity = max_integrity
        self.__power = power
        self.__finesse = finesse
        self.__integrity = self.__max_integrity
        self.__icebreaker = None

        if not isinstance(self.__max_integrity, int):
            print("Attenzione: max_integrity deve essere un intero. Corretto a 1.")
            self.__max_integrity = 1
        elif self.__max_integrity < 1:
            print("Attenzione: max_integrity deve essere >= 1. Corretto a 1.")
            self.__max_integrity = 1

        self.__integrity = self.__max_integrity

        if not isinstance(self.__power, int):
            print("Attenzione: power deve essere un intero. Corretto a 1.")
            self.__power = 1
        elif self.__power != max(1, min(20, self.__power)):
            print("Attenzione: power fuori range. Corretto.")

        self.__power = max(1, min(20, self.__power))

        if not isinstance(self.__finesse, int):
            print("Attenzione: finesse deve essere un intero. Corretto a 1.")
            self.__finesse = 1
        elif self.__finesse != max(1, min(20, self.__finesse)):
            print("Attenzione: finesse fuori range. Corretto.")

        self.__finesse = max(1, min(20, self.__finesse))

    def get_handle(self):
        return self.__handle

    def get_integrity(self):
        return self.__integrity

    def get_power(self):
        return self.__power

    def get_finesse(self):
        return self.__finesse

    def get_max_integrity(self):
        return self.__max_integrity

    def get_icebreaker(self):
        return self.__icebreaker

    def equip(self, icebreaker: Icebreaker) -> None:
        self.__icebreaker = icebreaker

    def modifier(self, value: int) -> int:
        return (value - 10) // 2

    def is_alive(self) -> bool:
        return self.__integrity > 0

    def take_damage(self, amount: int) -> int:
        if not isinstance(amount, int):
            print("Attenzione: amount deve essere un intero.")
            return 0
        elif amount < 0:
            print("Attenzione: amount deve essere >= 0.")
            return 0

        damage_taken = min(amount, self.__integrity)
        self.__integrity -= damage_taken
        return damage_taken

    def attack(self, enemy: "Runner") -> int:
        if self.__icebreaker is None:
            base_damage = 1
            damage_modifier = 0
        else:
            base_damage = self.__icebreaker.get_damage()
            if self.__icebreaker.get_type() == "fracter":
                damage_modifier = self.modifier(self.__power)
            else:
                damage_modifier = self.modifier(self.__finesse)

        total_damage = max(0, base_damage + damage_modifier)
        return enemy.take_damage(total_damage)

    def __str__(self) -> str:
        return f"{self.__handle} (Integrity: {self.__integrity}/{self.__max_integrity})"