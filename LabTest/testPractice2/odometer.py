

class Odometer(object):
    def __init__(self, mileage: float = 0.0, units: str = ''):
        if mileage < 0:
            raise ValueError(f"Mileage should be a positive number.")
        if units != 'km' or units != 'mi':
            raise ValueError(f"Units should be either km (Kilometers) or mi (Miles).")

        self.mileage = mileage
        self.units = units

    def __add__(self, other: float):
        if not isinstance(other, float):
            raise TypeError(f"Must be a number to perform addition.")

        return round(self.mileage + other, 1)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other: float):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Must be a number to perform subtraction.")
        if other > self.mileage:
            raise ValueError(f"Can only subtract a number less than the current mileage.")
        else:
            return round(self.mileage - other, 1)

    def __str__(self):
        return f"Mileage: {self.mileage:.1f} {self.units}"

o1 = Odometer(1200.45, 'km')
print(o1)

print(o1 + 505.50)
print(505.50 + o1)

print(o1 - 1000.00)

