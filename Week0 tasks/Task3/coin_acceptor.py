class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0
    def insertCoin(self):
        self.amount += 1
        self.value += 1
    def getAmount(self):    
        print(f"Currently '{self.value}' coins in coin acceptor")
    def returnCoins(self):
        print(f"Coin acceptor returned '{self.amount}' coins.")
        self.value = 0

