import math

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other):

        if isinstance(other, int):
            return Vector((self.x * other), (self.y * other))

        return (self.x * other.x) + (self.y * other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector with points (x: {self.x}, y: {self.y})"

v1 = Vector(1, 2)
v2 = Vector(2, 2)

print("\nTest Addition...")
v3 = v1 + v2
print("v1 + v2")
print(v3)

print("\nTest Multiplication...")
print("v1 * v2")
print(v1 * v2)
print("v1 * 3")
print(v1 * 3)

print("\nTest Subtraction...")
v4 = v1 - v2
print("v1 - v2")
print(v4)

print("\nTest Magnitude...")
print("v3 magnitude", v3.magnitude())

