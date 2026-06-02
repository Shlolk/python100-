class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    # Name (read-only)
    @property
    def name(self):
        return self._name

    # Health property
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    # Mana property
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    # Level property (read-only)
    @property
    def level(self):
        return self._level

    # Level up method
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

    # String representation
    def __str__(self):
        return (
            f"Name: {self._name}\n"
            f"Level: {self._level}\n"
            f"Health: {self._health}\n"
            f"Mana: {self._mana}"
        )
