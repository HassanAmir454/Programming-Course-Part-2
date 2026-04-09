from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod #decoration
    def __init__(self, legs: int):
        self.__legs = legs
        return None
    def countLegs(self) -> None:
        print(self.__legs)
        return None
