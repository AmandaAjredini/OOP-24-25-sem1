
class Colour(object):
    def __init__(self, red: float, blue: float, green: float):
        if not isinstance(red, float) or not isinstance(blue, float) or not isinstance(green, float):
            raise TypeError("All red, blue and green values must be a decimal-point number")

        if not (0 <= red <=1) or not (0 <= blue <=1) or not (0 <= green <=1):
            raise ValueError("All inputted values must be within the range of 0.0 - 1.0")

        self.red = red
        self.blue = blue
        self.green = green

    def saturate(self, value: float) -> float:
        """Saturate the value to ensure it remains within the [0, 1] range."""
        if value < 0:
            return 0.0
        elif value > 1:
            return 1.0
        return value

    def __add__(self, other):
        if not isinstance(other, Colour):
            raise TypeError("Addition can only be performed on Colour types.")

        new_red = self.saturate(self.red + other.red)
        new_blue = self.saturate(self.blue + other.blue)
        new_green = self.saturate(self.green + other.green)


        return Colour(new_red, new_blue, new_green)

    def __sub__(self, other):
        if not isinstance(other, Colour):
            raise TypeError("Subtraction can only be performed on Colour types.")

        new_red = self.saturate(self.red - other.red)
        new_blue = self.saturate(self.blue - other.blue)
        new_green = self.saturate(self.green - other.green)


        return Colour(new_red, new_blue, new_green)

    def __str__(self):
        return f"Red: {self.red:.3f}, Blue: {self.blue:.3f}, Green: {self.green:.3f}"

    def __repr__(self):
        return f"Colour(Red: {self.red:.3f}, Blue: {self.blue:.3f}, Green: {self.green:.3f})"


# Main Scope
c1 = Colour(0.4, 1.0, 0.67)
c2 = Colour(0.788, 0.456, 0.232)

print(c1 + c2)
print(c1 - c2)