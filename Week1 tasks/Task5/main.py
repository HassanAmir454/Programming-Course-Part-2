from entity import Entity, Player, NPC, Object, simulate_interactions

def main():
    entities = []
    print("Program starting.")
    while True:
        print("\nMenu:")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Choice: ")
        if choice == "1":
            print("\nSelect Entity Type:")
            print("1 - Player")
            print("2 - NPC")
            print("3 - Object")

            entity_type = int(input("Enter entity tyype here: "))
            name = input("Enter name of entity")
            x = int(input("Enter position of X: "))
            y = int(input("Enter position of Y: "))
            z = int(input("Enter position of Z: "))
            position = (x, y, z)
            if entity_type == 1:
                health = int(input("Enter health for Player: "))
                entities.append(Player(name, position, health))
                print("Player added.")
            elif entity_type == 2:
                role = input("Enter role for NPC: ")
                entities.append(NPC(name, position, role))
                print("NPC added.")
            elif entity_type == 3:
                collectible = input("Is collectible? (yes/no): ").lower() == "yes"
                entities.append(Object(name, position, collectible))
            else:
                print("Invalid entity type.")

        elif choice == "2":
            simulate_interactions(entities)
        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid menu choice.")
    print("Program ending.")
if __name__ == "__main__":
    main()            





                

