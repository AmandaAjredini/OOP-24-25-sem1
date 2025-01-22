
class Appliance(object):
    def __init__(self, brand: str, model: str, power_usage: float, status: bool = False):
        self.__brand = brand
        self.__model = model
        self._power_usage = power_usage
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def __str__(self):
        return (f"Brand: {self.__brand}\n"
                f"Model: {self.__model}\n"
                f"Power Usage: {self._power_usage}\n"
                f"Turned On: {self.status}\n")

class SmartAppliance(Appliance):
    def __init__(self, brand: str, model: str, power_usage: float, status: bool = False, wifi_enabled: bool = False):
        Appliance.__init__(self, brand, model, power_usage, status)
        self.__wifi_enabled = wifi_enabled
        self.__connected_devices = []

    def connect_device(self, new_device):
        if new_device in self.__connected_devices:
            print("Device already connected, choose another device to connect.")
            return

        self.__connected_devices.append(new_device)

    def disconnect_device(self, other):
        if other not in self.__connected_devices:
            print("Device you entered is not connected at the moment, choose another device to disconnect.")
            return

        self.__connected_devices.remove(other)

    def __str__(self):
        device_str = ''
        for device in self.__connected_devices:
            device_str += device
            print()

        return Appliance.__str__(self) + (f"WiFi Enabled: {self.__wifi_enabled}\n"
                                          f"Connected Devices: {device_str}\n")


class Room(object):
    def __init__(self, name: str, appliances: list = []):
        self.name = name
        self.appliances = appliances

    def add_appliance(self, appliance):
        if appliance not in self.appliances:
            self.appliances.append(appliance)
        else:
            print("Appliance already added, choose another appliance.")

    def total_power_usage(self):
        total_power_usage = 0

        for appliance in self.appliances:
            if appliance.status:
                total_power_usage += appliance._power_usage

        return total_power_usage

    def __add__(self, other):
        if not isinstance(other, Room):
            raise TypeError("Can only add Room objects")

        return Room(self.name + " & " + other.name, self.appliances + other.appliances)

    def __eq__(self, other):
        if not isinstance(other, Room):
            raise TypeError("Can only compare Room objects")

        if (self.name.lower() == other.name.lower()) and (len(self.appliances) == len(other.appliances)):
            return True
        else:
            return False

    def __str__(self):
        appliance_str = ''
        for appliance in self.appliances:
            appliance_str += Appliance.__str__(appliance) + f"\n"

        return (f"\nRoom: {self.name}\n"
                f"\nAppliances: \n{appliance_str}")


# Main Scope
sa1 = SmartAppliance(brand="Samsung", model="2024", power_usage=20000, status=False, wifi_enabled=True)
sa2 = SmartAppliance(brand="Philips", model="12v", power_usage=30000, status=False, wifi_enabled=True)

a1 = Appliance(brand="Sony", model="Pluto", power_usage=35000, status=False)

r1 = Room("Living Room", [sa1, sa2])
r2 = Room("Kitchen", [sa1, sa2])

sa1.turn_on()
sa2.turn_on()
a1.turn_on()

print(r1.total_power_usage())
print(r2.total_power_usage())

print(r1 + r2)
print(r1 == r2)

#print(dir(sa1))