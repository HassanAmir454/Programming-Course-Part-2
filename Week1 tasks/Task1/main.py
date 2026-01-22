from Iotdevices import TemperatureSensor, HumiditySensor, MotionSensor, IoTDevices

def main():
    devices = []

    while True:
        print("\n===== IoT Device Menu =====")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            dtype = input("Device type (TemperatureSensor/HumiditySensor/MotionSensor): ")
            did = input("Device ID: ")
            loc = input("Location: ")
            data = input("Data: ")

            if dtype.lower() == "temperaturesensor":
                devices.append(TemperatureSensor(did, loc, data))
            elif dtype.lower() == "humiditysensor":
                devices.append(HumiditySensor(did, loc, data))
            elif dtype.lower() == "motionsensor":
                devices.append(MotionSensor(did, loc, data))
            else:
                print("Invalid device type!")

        elif choice == "2":
            IoTDevices.serializing(devices)
            print("Data serialized.")

        elif choice == "3":
            devices = IoTDevices.deserializing()
            print("Data deserialized.")

        elif choice == "4":
            IoTDevices.encryption()
            print("Data encrypted.")

        elif choice == "5":
            IoTDevices.decryption()
            print("Data decrypted.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid menu choice!")
    print("\nProgram ending")

if __name__ == "__main__":
    main()
