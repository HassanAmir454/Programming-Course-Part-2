class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0
    def insertCoin(self, user_choice):
        self.amount += 1
        self.value += user_choice
        print(f"Inserted coins = {self.amount}, value = {self.value}€")

    def getAmount(self):    
        print(f"Currently '{self.value}' coins in coin acceptor")
    def returnCoins(self)-> tuple[int, float]:
        print(f"{self.amount} coins with {self.value}€ value returned.")
        self.amount = 0
        self.value = 0
        print(f"Inserted coins = {self.amount}, value = {self.value}€")
