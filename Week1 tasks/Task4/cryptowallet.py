class CryptoWallet:
    def __init__(self, walletId):
        self.__balance = 0
        self.__walletId = walletId
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        self.__balance -= amount
        self.__transactions.append(f"Withdrawed {amount}")

    def check(self):
        return self.__balance
    
    def get_walletId(self):
        return self.__walletId

    def get_transaction_history(self) -> list:
        return self.__transactions.copy()