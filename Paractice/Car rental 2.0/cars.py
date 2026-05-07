from vehicles import Vehicle 


class Cars(Vehicle):

    def vehicle_type(self):
        print(f"{self._name} is a Car")
        
    def calculate_rent(self, days):
        if days > 5:
            discount = self._price_per_day * 10/100
            rent = (self._price_per_day*days) - discount
            print(f" Rent = {rent}")
        else:
            rent = (self._price_per_day*days)
            print(f" Rent = {rent}")



        

