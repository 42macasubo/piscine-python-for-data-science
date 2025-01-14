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
