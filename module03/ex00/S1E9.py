from abc import ABC, abstractmethod


class Character(ABC):
    """Character doc"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Character init doc"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """die doc"""
        self.is_alive = False

class Stark(Character):
    """Stark doc"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark init doc"""
        super().__init__(first_name, is_alive)


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

#    hodor = Character('hodor')

if __name__ == '__main__':
    main()
