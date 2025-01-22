class Hero(object):
   """Basic template for hero. Contains name, power level and health
   points attributes. Implements the punch methods and string method."""


   def __init__(self, name="", power_level=1, health_points=100):
       self.__name = name
       self.health_points = health_points
       self.power_level = power_level


   def punch(self) -> float:
       """Return the punch power, which is 2 times the heroes level"""
       return self.power_level * 2


   def __str__(self):
       hero_info = f"Name: {self.__name}\n"
       hero_info += f"Power level: {self.power_level}\n"
       hero_info += f"Health points: {self.health_points}\n"


       return hero_info


class Archer(Hero):
    def __init__(self, name="", power_level=1, health_points=100, arrows=10):
        Hero.__init__(self, name, power_level, health_points)
        self.arrows = arrows

    def attack(self) -> float:

        if self.arrows == 0:
            return 0

        max_attack = 100
        return self.power_level/100 * max_attack

    def defense(self):
        self.health_points += 10

    def combat(self, monster):

        if not isinstance(monster, Monster):
            print("Hero only fights monsters!")
            return

        while True:
            monster.health_points -= self.attack()

            if monster.health_points <= 0:
                print("Hero wins the fight")
                return True

            self.health_points -= monster.attack()

            if self.health_points <= 0:
                print("Hero loses the fight")
                return False

class Monster(object):

    def __init__(self, name: str, strength: float, health_points: float, roar: str):
        self.name = name
        self.strength = strength
        self.health_points = health_points
        self.roar = roar

        print(self.roar)

    def attack(self) -> float:
        return self.strength * 2

    def __add__(self, other):

        new_name = self.name + other.name
        new_strength = self.strength * other.strength
        new_health_points = self.health_points + other.health_points
        new_roar = self.roar + other.roar + "!!!"

        return Monster(new_name, new_strength, new_health_points, new_roar)

# Main Scope
legolas = Archer("Legolas", 50, 200, 200)
orc = Monster("Orc", 30, 100, "Arrr")
warg = Monster("Warg", 40, 120, "Ooarrh")

orcWarg = orc + warg

if legolas.combat(orc):
    print("Orc is down")
else:
    print("Game over!")
    exit()

legolas.defense()
legolas.defense()
legolas.defense()
legolas.defense()

if legolas.combat(warg):
    print("Warg is down")
else:
    print("Game over")
    exit()

if legolas.combat(orcWarg):
    print("Legal beats all monsters!")
else:
    print("Game over!")
    exit()