from coin_acceptor import CoinAcceptor

ca = CoinAcceptor()

 

def main()-> None:
    print("Program starting.")
    print("Initializing counter")
    print("Counter initialized.\n")
    while True:
        print("Options:")
        print("1) Insert coin")
        print("2) Show coins")
        print("3) Return coins")
        print("0) Exit program")
        user_choice = input("Choice: ")
        if user_choice == "1":           
            ca.insertCoin()
        elif user_choice == "2":
            ca.getAmount()
        elif user_choice == "3":
            ca.returnCoins()
        elif user_choice == "0":
            break
        else: 
            print("Enter valid input!")
    print("Program ending")

main()
