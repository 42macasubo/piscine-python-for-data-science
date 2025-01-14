from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """doc King"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """doc King init"""
        super().__init__(first_name, is_alive)


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

if __name__ == '__main__':
    main()
