from temperature_converter import TemperatureConverter

tc = TemperatureConverter()

def main()-> None:
    print("Program starting.")
    print("Initializing temperature converter...")
    print("Temperature converter initialized.\n")
    while True:
        print("Options:")
        print("1) Set temperature")
        print("2) Convert to Celsius")
        print("3) Convert to Fahrenheit")
        print("4) Convert to Kelvin")
        print("0) Exit program")
        user_choice = input("Choice: ")
        if user_choice == "1":
            temp = float(input("Enter temperature:"))
            tc.setTemperature(temp)
            print("Temperature set to {temp}")
        elif user_choice == "2":
            tc.toCelcious()
        elif user_choice == "3":
            tc.toFahrenheit()
        elif user_choice == "4":
            tc.toKelvin()
        elif user_choice == "0":
            break
        else: 
            print("Enter valid input!")
    print("Program ending")

main()

