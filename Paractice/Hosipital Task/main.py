from hospital import Doctor, Nurse, Technician, add_members, read_members, list_members

def main():
    members = []  # This will store all HospitalMember objects

    while True:
        print("\n--- Smart Hospital Management System ---")
        print("1 - Add Staff Member")
        print("2 - List Staff Members")
        print("3 - Perform Duties")
        print("4 - Save Members to File")
        print("5 - Load Members from File")
        print("0 - Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter name of member: ")
                role = input("Doctor/Nurse/Technician?")
                extra = input("Specialization/Ward/Equipment: ")
                members.append({name, role, extra})

                

            elif choice == 2:
                list_members(members)
                

            elif choice == 3:
                name = input("Enter name of member: ")
                for member in members:
                    if member[0] == name:
                        member[1].perform_duty()           

            elif choice == 4:
                if members:
                    add_members(members)
                else:
                    print("Not memebers fount")

                

            elif choice == 5:
                members = read_members()
                

            elif choice == 0:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid menu choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()