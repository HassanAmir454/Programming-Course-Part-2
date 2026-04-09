from rent import Car, Bike, Truck, RentalCompany

company = RentalCompany()

while True:
    print("\n1 Add Vehicle")
    print("2 List Vehicles")
    print("3 Rent Vehicle")
    print("4 Return Vehicle")
    print("5 Calculate Rent")
    print("6 Save")
    print("7 Load")
    print("0 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vtype = input("Car/Bike/Truck: ")

        vid = input("Vehicle ID: ")
        price = int(input("Price per day: "))

        if vtype == "Car":
            brand = input("Brand: ")
            seats = int(input("Seating capacity: "))
            vehicle = Car(vid, price, brand, seats)

        elif vtype == "Bike":
            cc = int(input("Engine CC: "))
            helmet = input("Helmet included (yes/no): ") == "yes"
            vehicle = Bike(vid, price, cc, helmet)

        elif vtype == "Truck":
            load = int(input("Load capacity: "))
            vehicle = Truck(vid, price, load)

        company.add_vehicle(vehicle)

    elif choice == "2":
        company.list_vehicles()

    elif choice == "3":
        vid = input("Vehicle ID: ")
        company.rent_vehicle(vid)

    elif choice == "4":
        vid = input("Vehicle ID: ")
        company.return_vehicle(vid)

    elif choice == "5":
        vid = input("Vehicle ID: ")
        days = int(input("Number of days: "))
        company.calculate_rent(vid, days)

    elif choice == "6":
        company.save_to_file()

    elif choice == "7":
        company.load_from_file()

    elif choice == "0":
        break

    else:
        print("Invalid choice.")
