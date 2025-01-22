
class Compass(object):
    def __init__(self, degrees: int = 0, minutes: int = 0):
        if not isinstance(degrees, int) or not isinstance(minutes, int):
            raise TypeError("Both degrees and minutes should be integers.")

        if not (0 <= degrees < 360) or not (0 <= minutes < 60):
            raise ValueError("Degrees must be between (0 - 359) and minutes must be between (0 - 59).")

        self.degrees = degrees
        self.minutes = minutes

    def __add__(self, other):
        if isinstance(other, Compass):
            total_minutes = self.degrees * 60 + self.minutes + other.degrees * 60 + other.minutes
        elif isinstance(other, int):  # Adding an integer (degrees)
            total_minutes = self.degrees * 60 + self.minutes + other * 60
        else:
            raise TypeError("Addition can only be performed with another Compass or an integer.")

        # Normalize the result to handle overflow of minutes and degrees
        total_degrees = (total_minutes // 60) % 360  # Wrap degrees between 0 and 359
        total_minutes = total_minutes % 60  # Ensure minutes is between 0 and 59

        return Compass(total_degrees, total_minutes)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"{self.degrees}° {self.minutes}'"



# Main Scope
c1 = Compass(270, 36)
c2 = Compass(90, 45)

print(c1)  # Output: 270° 36'
print(c2)  # Output: 90° 45'

# Addition of two compass bearings
c3 = c1 + c2
print(c3)  # Output: 361° 81', but after adjustment, 2° 21'

# Addition of compass bearing and integer (degrees)
c4 = c1 + 90
print(c4)  # Output: 360° 36'

# Demonstrating commutative addition (integer + compass)
c5 = 90 + c1
print(c5)  # Output: 360° 36'