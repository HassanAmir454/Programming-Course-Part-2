class SmartDevice:
    def __init__(self, name, status=False):
        self.DeviceName = name
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False


class SmartLight(SmartDevice):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def set_color(self, color):
        self.color = color
    
    def operate(self):
        if self.status:
            return f"{self.DeviceName} is shining {self.color} light"
        return f"{self.DeviceName} is turned off"


class SmartThermostat(SmartDevice):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
    
    def operate(self):
        if self.status:
            return f"{self.DeviceName} is maintaining temperature at {self.temperature}°C."
        return f"{self.DeviceName} is turned off"


class SmartLock(SmartDevice):
    def __init__(self, name, locked=True):
        super().__init__(name)
        self.locked = locked

    def lock(self):
        self.locked = True
    
    def unlock(self):
        self.locked = False

    def operate(self):
        state = "locked" if self.locked else "unlocked"
        return f"{self.DeviceName} is curently {state}"

def operate_devices(devices):
    if not devices:
        print("No device to operate")
        return
    for device in devices:
        print(device.operate())