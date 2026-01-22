from counter import Counter 
c = Counter()
def main()-> None:
    print("Program starting.")
    print("Initializing counter")
    print("Counter initialized.\n")
    while True:
        print("Options:")
        print("1) Add count")
        print("2) Get count")
        print("3) Zero count")
        print("0) Exit program")
        user_choice = input("Choice: ")
        if user_choice == "1":
            amount = int(input("How much amount: "))
            c.add_count(amount)
        elif user_choice == "2":
            print(f"Your current count is {c.get_count()}")
        elif user_choice == "3":
            c.zero_count()
        elif user_choice == "0":
            break
        else: 
            print("Enter valid input!")
    print("Program ending")

main()




