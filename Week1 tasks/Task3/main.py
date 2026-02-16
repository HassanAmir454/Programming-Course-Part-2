from smartdevice import SmartLight, SmartThermostat, SmartLock, operate_devices


def main():
    devices = []

    while True:
        print("\nSmart Home Menu")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\nChoose device type:")
            print("1 - Smart Light")
            print("2 - Smart Thermostat")
            print("3 - Smart Lock")
            device_type = input("Enter device type: ")
            name = input("Enter device name: ")
            if device_type == "1":
                color = input("Enter color for light: ")
                device = SmartLight(name, color)
            
            elif device_type == "2":
                temperature = float(input("Enter temperature for device: "))
                device = SmartThermostat(name, temperature)
            
            elif device_type == "3":
                device = SmartLock(name)
            
            else:
                print("Invalid device type.")
                continue
            device.turn_on()
            devices.append(device)
            print(f"{name} added successfully.")

        elif choice == 2:
            operate_devices(devices)
        
        elif choice == 0:
            print("Exiting program")
            break
    print("Program ending.")

if __name__ == "__main__":
    main()




