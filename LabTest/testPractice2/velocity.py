class Velocity:
    def __init__(self, distance: float = 0.0, time: float = 1.0, unit: str = 'm/s'):
        """
        Constructor that can initialize the velocity in meters per second by default.
        If distance, time, and unit are provided, it calculates the velocity and converts if needed.
        """
        if unit == 'ft/s':
            # Convert feet/sec to meters/sec
            self.speed = (distance / time) * 0.3048
        elif unit == 'm/s':
            self.speed = distance / time
        else:
            raise ValueError("Unit must be either 'm/s' or 'ft/s'.")

    def __str__(self):
        """ String representation of the velocity in meters/sec. """
        return f"{self.speed:.2f} m/s"

    def __repr__(self):
        """ Representation for debugging purposes. """
        return f"Velocity({self.speed:.2f})"

    def __pos__(self):
        """ Unary operator: returns the absolute value of the velocity (speed). """
        return Velocity(abs(self.speed))

    def __add__(self, other):
        """ Addition of velocities (in meters/second). """
        if isinstance(other, Velocity):
            return Velocity(self.speed + other.speed)
        elif isinstance(other, (int, float)):  # Adding a scalar to the velocity.
            return Velocity(self.speed + other)
        else:
            raise TypeError("Can only add another Velocity or a scalar (int/float)")

    def __radd__(self, other):
        """ Reverse addition (scalar + Velocity). """
        return self.__add__(other)

    def __sub__(self, other):
        """ Subtraction of velocities (in meters/second). """
        if isinstance(other, Velocity):
            return Velocity(self.speed - other.speed)
        elif isinstance(other, (int, float)):  # Subtracting a scalar from the velocity.
            return Velocity(self.speed - other)
        else:
            raise TypeError("Can only subtract another Velocity or a scalar (int/float)")

    def __rsub__(self, other):
        """ Reverse subtraction (scalar - Velocity). """
        return Velocity(other - self.speed)

# Sample Usage:

v1 = Velocity(100, 10, 'm/s')  # 100 meters in 10 seconds
v2 = Velocity(300, 10, 'ft/s')  # 300 feet in 10 seconds, which will be converted to meters/sec

print(v1)  # Output: 10.00 m/s
print(v2)  # Output: 9.14 m/s (converted from feet/sec to meters/sec)

# Demonstrating operator overloads:
v3 = v1 + v2  # Adding two velocities
print(v3)  # Output: 19.14 m/s

v4 = v1 - v2  # Subtracting two velocities
print(v4)  # Output: 0.86 m/s

v5 = +v1  # Unary plus to get absolute velocity (should remain the same for positive velocities)
print(v5)  # Output: 10.00 m/s
