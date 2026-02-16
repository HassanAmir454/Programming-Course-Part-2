class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def interact(self):
        raise NotImplementedError("Subclasses must implement interact()")

class Player(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position)
        self.health = health
    def interact(self):
        print(f"Player {self.name} explores the environment at {self.position}.")
class NPC(Entity):
    def __init__(self, name, position, role):
        super().__init__(name, position)
        self.role = role
    def interact(self):
        print(f"NPC {self.name} ({self.role}) offers a quest.")
class Object(Entity):
    def __init__(self, name: str, position: tuple, is_collectible: bool):
        super().__init__(name, position)
        self.is_collectible = is_collectible
    def interact(self):
        if self.is_collectible:
            print(f"Object {self.name} can be picked up.")
        else:
            print(f"Object {self.name} is part of the environment.")  
def simulate_interactions(entities):
    if not entities:
        print("No entities to interact with")
    for entity in entities:
        entity.interact()



