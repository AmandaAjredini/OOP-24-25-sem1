import random

class Island(object):
    """ Island n X n grid where zero value indicates an unoccupied cell. """

    def __init__(self, n: int, prey_count=0, pred_count=0):
        """ Initialise cell to all 0's, the fill with animals """

        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0] * n  # row is a list of n zeros
            self.grid.append(row)
        self.init_animals(prey_count,pred_count)

    def animal(self, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        else:
            return -1

    def init_animals(self, prey_count, pred_count):
        count = 0
        while count < prey_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_prey = Prey(island=self, x=x, y=y)
                count += 1
                self.register(new_prey)

        count = 0
        while count < pred_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_pred = Predator(island=self, x=x, y=y)
                count += 1
                self.register(new_pred)

    def size(self):
        """ Return size of the island """
        return self.grid_size

    def register(self, animal):
        """ Register animal with island """
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def remove(self, x, y):
        self.grid[x][y] = 0

    def __str__(self):
        """ String representation for printing """

        s = ""
        for j in range(self.grid_size - 1, -1, -1):  # print row size−1 first
            for i in range(self.grid_size):  # each row starts at 0
                if not self.grid[i][j]:
                # print a ' . ' for an empty space
                    s += "{:<3s}".format('.' + " ")
                else:
                    s += "{:<3s}".format((str(self.grid[i][j])) + " ")
            s += "\n"
        return s

class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        self.island = island
        self.name = s
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y

    def __str__(self):
        return self.name

class Prey(Animal):
    def __init__(self, island, x=0, y=0, s="0"):
        Animal.__init__(self, island, x, y, s)

    def move(self):
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]

            if self.island.animal(x, y) == 0:
                self.island.remove(self)
                self.x = x
                self.y = y
                self.island.register(self)
                break

    def __str__(self):
        return Animal.__str__(self)

class Predator(Animal):
    def __init__(self, island, x=0, y=0, s="X"):
        Animal.__init__(self, island, x, y, s)

    def __str__(self):
        return Animal.__str__(self)

# Main Scope
royale = Island(10)
animal1 = Animal(royale, 4, 8, "a1")
print(animal1.position())
animal2 = Animal(royale, 6, 4, "a2")
royale.register(animal1)
royale.register(animal2)
print(royale)