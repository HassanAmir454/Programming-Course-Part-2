from gamecharacter import GameCharacter, Warrior, Mage, Archer, simulate_battle

def main():
    characters = []
    print("Program starting.")
    while True:
        print("\n1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            ctype = input("Enter character type (Warrior/Mage/Archer): ").strip()
            cname = input("Enter character name: ").strip()

            if ctype.lower() == "warrior":
                characters.append(Warrior(cname))
                print(f"Warrior {cname} created!\n")
            elif ctype.lower() == "mage":
                characters.append(Mage(cname))
                print(f"Mage {cname} created!\n")
            elif ctype.lower() == "archer":
                characters.append(Archer(cname))
                print(f"Archer {cname} created!\n")
            else:
                print("Invalid character type! Please choose Warrior, Mage, or Archer.\n")

        elif choice == "2":
            simulate_battle(characters)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid menu choice! Please enter 0, 1, or 2.\n")
    print("\nProgram ending")

if __name__ == "__main__":
    main()



