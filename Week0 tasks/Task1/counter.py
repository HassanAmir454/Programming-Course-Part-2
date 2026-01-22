class Counter:
    def __init__(self):
        self.count = 0
    def add_count(self, amount):
        self.count += amount
        print("Count Increased.")
    def get_count(self):
        # print(f"Your count is: {self.count}")
        return self.count
    def zero_count(self):
        self.count = 0
        print("Count zeroed")


