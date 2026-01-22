class IoTDevices:
    def __init__(self, deviceid, location, data):
        self.deviceid = deviceid
        self.location = location
        self.data = data

    def to_csv(self):
        return f"{self.__class__.__name__},{self.deviceid},{self.location},{self.data}"
    @staticmethod
    def from_csv(line):
        device_type, deviceid, location, data = line.strip().split(",")
        if device_type == "TemperatureSensor":
            return TemperatureSensor(deviceid, location, data)
        elif device_type == "HumiditySensor":
            return HumiditySensor(deviceid, location, data)
        elif device_type == "MotionSensor":
            return MotionSensor(deviceid, location, data)
        else:
            raise ValueError("Unknown device type")
    @staticmethod
    def serializing(devices, filename="devices.csv"):
        with open(filename, "w") as file:
            for device in devices:
                file.write(device.to_csv() + "\n")
    @staticmethod
    def deserializing(filename="devices.csv"):
        devices = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    devices.append(IoTDevices.from_csv(line))
        except FileNotFoundError:
            print("File not found.")
        return devices
    @staticmethod
    def encryption(filename="devices.csv", enc_file="devices.enc"):
        try:
            with open(filename, "r") as file:
                data = file.read()

            encrypted_data = ""
            for c in data:
                asi_num = ord(c) + 2
                new_character = chr(asi_num)
                encrypted_data+=new_character
            with open(enc_file, "w") as file:
                file.write(encrypted_data)
        except FileNotFoundError:
            print("File not found for encryption.")
    @staticmethod
    def decryption(enc_file="devices.enc", dec_file="devices_dec.csv"):
        try:
            with open(enc_file, "r") as file:
                data = file.read()

            decrypted_data = ""
            for c in data:
                asi_num = ord(c) - 2
                new_character = chr(asi_num)
                decrypted_data+=new_character
            with open(dec_file, "w") as file:
                file.write(decrypted_data)
        except FileNotFoundError:
            print("File not found for encryption.")

class TemperatureSensor(IoTDevices):
    pass


class HumiditySensor(IoTDevices):
    pass


class MotionSensor(IoTDevices):
    pass


