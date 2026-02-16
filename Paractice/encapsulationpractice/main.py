from account import BankAccount, SavingsAccount, CurrentAccount, Display_all_acc

def main()-> None:
    Accounts = []
    print("Program starting.")
    print("Welcome to Apna Bank")
    while True:
        print("Options:")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Display_info")
        print("4) Calculate_interest")
        print("5) Display_all_acc")
        print("0) Exit")
        user_choice = input("Choice: ")
        account_no = int(input("Enter your account number: "))

        if user_choice == "1":
        
            balance = int(input("Enter amount for deposit: "))
            account = BankAccount(account_no).deposit(balance)
            Accounts.append(account)

        elif user_choice == "2":
            amount = int(input("Enter amount for withdraw: "))
            account = BankAccount(account_no).withdraw(amount)
            Accounts.append(account)
        elif user_choice == "3":
            account_no = int(input("Enter your account number: "))
            BankAccount(account_no).display_info()
        elif user_choice == "4":
            SavingsAccount().calculate_interest()
        elif user_choice == "5":
            Display_all_acc(Accounts)
        elif user_choice == "0":
            break
        else: 
            print("Enter valid input!")
    print("Program ending")

main()

