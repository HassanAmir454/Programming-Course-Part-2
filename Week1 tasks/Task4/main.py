from cryptowallet import CryptoWallet



def main():
    wallets = {}
    print("Program starting")
    while True:
        print("\nSmart Home Menu")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            walletId = input("Enter wallet Id: ")
            if walletId in wallets:
                print(f"{walletId} wallet Id already exits.")
            else:
                wallets[walletId] = (CryptoWallet(walletId))
                print("Wallet created successfully.")

        elif choice == 2:
            walletId = input("Enter wallet ID: ")
            amount = float(input("How much amount you want to deposit: "))
            wallets[walletId].deposit(amount)
            print("Deposit successful.")
        
        elif choice == 3:
            walletId = input("Enter wallet ID: ")
            amount = float(input("Enter how much amount you want to withdraw: "))
            wallets[walletId].withdraw(amount)
            print("Withdrawal successful.")
        
        elif choice == 4:
            walletId = input("Enter wallet ID: ")
            balance = wallets[walletId].check()
            print(f"Balance: {balance}")

        elif choice == "5":
                wallet_id = input("Wallet ID: ")
                history = wallets[wallet_id].get_transaction_history()
                if not history:
                    print("No transactions found.")
                else:
                    for t in history:
                        print("-", t)

        elif choice == "0":
                print("Program ending.")
                break

        else:
                print("Invalid menu choice.")
    print("Program ending")

if __name__ ==  "__main__":
    main()


            
