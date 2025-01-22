class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def add_car(self, car_type: int) -> bool:
        if car_type == 1:
            if 0 < self.big < 1000:
                self.big -= 1
                return True
            else:
                return False

        if car_type == 2:
            if 0 < self.medium < 1000:
                self.medium -= 1
                return True
            else:
                return False

        if car_type == 3:
            if 0 < self.small < 1000:
                self.small -= 1
                return True
            else:
                return False

# Main Scope
# Your ParkingSystem object will be instantiated and called as such:
ps = ParkingSystem(1, 1, 0) # spaces available in each part
print(ps.add_car(1))
print(ps.add_car(2))
print(ps.add_car(3))
print(ps.add_car(1))