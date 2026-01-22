class TemperatureConverter:
    def __init__(self):
        self.temperature : 0.0

    def setTemperature(self,temp:float)->None:
        self.temperature = temp

    def toCelcious(self)->float:
        celcious = self.temperature
        print(f"Temperature in Celsius: {celcious}°C")
    def toFahrenheit(self)->float:
        fahrenheit = (self.temperature*(9/5))+32
        print(f"Temperature in Fahrenheit: {fahrenheit}°F")
    def toKelvin(self)->float:
        kelvin = self.temperature+273.15
        print(f"Temperature in Kelvin: {kelvin}K")
    



