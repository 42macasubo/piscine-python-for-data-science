from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """doc Baratheon init"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def set_eyes(self, color: str) -> None:
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        self.hairs = color

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs

class Lannister(Character):
    """doc lannister"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """doc Lannister init"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """doc create_lannister"""
        return cls(first_name, is_alive)
