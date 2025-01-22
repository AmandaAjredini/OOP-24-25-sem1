# class TestClass(object):
#     def __init__(self,param_str=''):
#         self.the_str=''
#         for c in param_str:
#             if c.isalpha():
#                 self.the_str += c
#     def __add__(self,param):
#         if type(param)==TestClass:
#             the_str = self.the_str + param.the_str
#             return TestClass(the_str)
#         else:
#             return self
#     def __str__(self):
#         return 'Value: {}'.format(self.the_str)
#
# inst1 = TestClass('abc')
# inst2 = TestClass('123ijk')
# sumInst1 = inst1 + inst2
# sumInst2 = inst1 + 'xyz'
# print(inst1) # Line 1
# print(sumInst1) # Line 2
# print(sumInst2) # Line 3
# print(isinstance(sumInst2,TestClass)) # Line 4

class Vehicle(object):
    """Base class for a vehicle. Contains make, model, fuel level, and max speed."""

    def __init__(self, make: str, model: str, max_speed: float, fuel_level: float = 100):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def __str__(self):
        return f"{self.make} {self.model}, Max Speed: {self.max_speed} km/h, Fuel Level: {self.fuel_level}%"


class SUV(Vehicle):
    """ Class for a SUV (type of vehicle)"""

    def __init__(self, make: str, model: str, max_speed: float, fuel_level: float = 100, panoramic_sunroof=False):
        Vehicle.__init__(self, make, model, max_speed, fuel_level)
        self.panoramic_sunroof = panoramic_sunroof

    def speed(self, distance: float, time: float) -> float:
        return distance / time

    def refuel(self):
        self.fuel_level = 100

    def drive_to_signal(self, other) -> bool:
        if not isinstance(other, TrafficSignal):
            raise TypeError("The vehicle can only interact with traffic signals.")

        if other.colour == "green":
            print("Vehicle is driving past the signal.")
            return True
        else:
            print("Vehicle is not driving past the signal.")
            return False

    def __str__(self):
        return Vehicle.__str__(self) + f", Panoramic Sunroof: {self.panoramic_sunroof}"

class TrafficSignal(object):
    """ Class for a traffic signal """
    def __init__(self, colour: str, duration: int, location: str):
        self.colour = colour
        self.duration = duration
        self.location = location

    def change_signal(self, new_colour: str):
        self.colour = new_colour
        print(f"Colour changed to {self.colour}")

    def __add__(self, other):
        return TrafficSignal("yellow", (self.duration + other.duration), (self.location + "&" + other.location))

    def __str__(self):
        return f"Current Signal Info: Colour: {self.colour}, Duration: {self.duration}, Location: {self.location}"


# Main Scope
s1 = SUV("Audi", "RS6", 350.00, 60.80, True)
print(s1)

ts1 = TrafficSignal("red", 10, "top")
ts2 = TrafficSignal("yellow", 4, "middle")
ts3 = TrafficSignal("green", 8, "bottom")
ts4 = ts1 + ts2
print(ts4)

s1.drive_to_signal(ts1)
s1.drive_to_signal(ts2)
s1.drive_to_signal(ts3)