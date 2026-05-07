from file_handler import FileHandler
from cars import Cars
from bikes import Bikes
from vehicles import Vehicle

def deserialization(row):
    columns = row.split(",")

    if len(columns) < 4:
        print("Skipping bad row:", row)
        return None

    v_type = columns[0]
    name = columns[1]
    price = int(columns[2])
    wheels = int(columns[3])

    if v_type == "Car":
        return Cars(name, price, wheels)
    elif v_type == "Bike":
        return Bikes(name, price, wheels)

def main():
    filename = "vehicles.csv"
    file = FileHandler(filename)
    rows = file.read()

    vehicles = []
    for row in rows:
        vehicle = deserialization(row)

        if vehicle is not None:
            vehicles.append(vehicle)
    print("\n===== Vehicle System =====")
    while True:
        print("\nMenu:")
        print("1 - Display all vehicles")
        print("2 - Rent vehicle")
        print("3 - Update price")
        print("4 - Save changes")
        print("0 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for v in vehicles:
                v.display_info()
                v.vehicle_type()
        elif choice == "2":
            name = input("Enter name of vehicle:")
            days = int(input("How much days do you wanna rent: "))

            found = False
            for v in vehicles:
                if v._name == name:
                    v.calculate_rent(days)
                    found = True
                    break
            if not found:
                print("Vehicle not found")

        elif choice == "3":
            name = input("Enter name of vehicle:")
            price = int(input("Enter new price: "))

            found = False
            for v in vehicles:
                if v._name == name:
                    v._price_per_day = price
                    found = True
                    break
            if not found:
                print("Vehiclke not found")



        elif choice == "4":
            file.write(vehicles)
            print("Data saved to file")

        # 🔹 Exit
        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()




    
    


    