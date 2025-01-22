
class Animal:
    """Base class for animals. Contains name, weight, and age attributes."""

    def __init__(self, name: str, weight: float, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Weight: {self.weight} kg\n"
                f"Age: {self.age} years\n")

class Cat(Animal):
    """ Class for cat (type animal)"""

    def __init__(self, name: str, weight: float, age: int, breed: str):
        Animal.__init__(self, name, weight, age)
        self.breed = breed

    def print_sound(self):
        print("Meow!")

    def daily_food(self) -> float:
        return self.weight * 0.1

    def explore_habitat(self, other):
        if not isinstance(other, Habitat):
            raise TypeError("Animals can only explore habitats.\n")

        if other.type == "Forest":
            print(f"Cats thrive in this habitat\n")
        else:
            print(f"Cats cannot thrive in this habitat\n")

    def __str__(self):
        return Animal.__str__(self) + f"Breed: {self.breed}\n"

class Habitat(object):
    """ Class for habitat """
    def __init__(self, type: str, area: float, climate: str):
        self.type = type
        self.area = area
        self.climate = climate

    def expand_area(self, amount):
        self.area += amount

    def __add__(self, other):
        if not isinstance(other, Habitat):
            raise TypeError("Addition can only add Habitat objects.")

        return Habitat((self.type + "&" + other.type), (self.area + other.area), "Mixed")

    def __str__(self):
        return (f"Type: {self.type}\n"
                f"Area: {self.area}\n"
                f"Climate: {self.climate}\n")


# Main Scope
c1 = Cat("Luna", 3.45, 3, "Scottish Fold")

h1 = Habitat("Rainforest", 2200, "Humid")
h2 = Habitat("Forest", 220, "Tropical")
h3 = Habitat("Dessert", 1560, "Dry")

h4 = h2 + h3

print(h1)
c1.explore_habitat(h1)

print(h2)
c1.explore_habitat(h2)

print(h3)
c1.explore_habitat(h3)
