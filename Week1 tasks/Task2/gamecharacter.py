from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def defend(self):
        pass
class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks")
    def defend(self):
        print(f"{self.name} defends")
class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks")
    def defend(self):
        print(f"{self.name} defends")
class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks")
    def defend(self):
        print(f"{self.name} defends")

def simulate_battle(characters):
    if not characters:
        print("No characters available for battle.")
        return
    print("--- Battle Starts! ---\n")
    for char in characters:    
        char.attack()
        char.defend()

    print("--- Battle End! ---\n")
        


    


