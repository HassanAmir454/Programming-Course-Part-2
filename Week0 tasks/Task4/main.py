from cli_coinacceptor import CoinAcceptor

ca = CoinAcceptor()

 

def main()-> None:
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")

    while True:
       
        user_choice = float(input("Insert coin(0 return, -1 exit): "))
        
        if user_choice > 0:           
            ca.insertCoin(user_choice)
            print("Inserting...")
            
         
        elif user_choice == 0:
            ca.returnCoins()


        elif user_choice == -1:
            print("Exiting program.")
            break
        else: 
            print("Enter valid input!")
    print("\nProgram ending")

main()