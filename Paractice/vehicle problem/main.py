from vehicles import Car, Bike, ElectricScooter, operate_vehicles


def main():
    vehicles = []

    while True:
        print("\n--- Smart Vehicle System ---")
        print("1 - Add Vehicle")
        print("2 - Operate Vehicles")
        print("0 - Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\nChoose vehicle type:")
                print("1 - Car")
                print("2 - Bike")
                print("3 - Electric Scooter")

                vehicle_type = int(input("Enter vehicle type: "))
                name = input("Enter vehicle name: ")

                if vehicle_type == 1:
                    fuel = float(input("Enter fuel level: "))
                    vehicle = Car(name, fuel)

                elif vehicle_type == 2:
                    gear = int(input("Is bike in gear? (1 = Yes, 0 = No): "))
                    vehicle = Bike(name, gear)

                elif vehicle_type == 3:
                    battery = float(input("Enter battery level: "))
                    vehicle = ElectricScooter(name, battery)

                else:
                    print("Invalid vehicle type.")
                    continue

                vehicle.start()
                vehicles.append(vehicle)
                print(f"{name} added successfully.")

            elif choice == 2:
                operate_vehicles(vehicles)

            elif choice == 0:
                print("Exiting program.")
                break

            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Please enter valid numeric input.")


if __name__ == "__main__":
    main()
