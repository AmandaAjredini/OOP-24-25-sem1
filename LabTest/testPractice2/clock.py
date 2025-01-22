
class Clock(object):
    def __init__(self, hrs, mins, secs):
        if not (0 <= hrs < 24) or not (0 <= mins < 60) or not (0 <= secs < 60):
            print(f"Creating a Clock instance with 0 hours, 0 minutes, 0 seconds.")
            self.hrs = 0
            self.mins = 0
            self.secs = 0
        else:
            self.hrs = hrs
            self.mins = mins
            self.secs = secs

    def __add__(self, other):
        if isinstance(other, Clock):
            new_secs = self.secs + other.secs
            new_mins = self.mins + other.mins + new_secs // 60
            new_hrs = self.hrs + other.hrs + new_mins // 60

            return Clock(new_hrs % 24, new_mins % 60, new_secs % 60)

        elif isinstance(other, int):
            new_hrs = self.hrs + other
            return Clock(new_hrs % 24, self.mins, self.secs)
        
        else:
            raise TypeError(f"Addition can only be performed with another Clock type or an integer(hours).")

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"{self.hrs}hrs, {self.mins}mins, {self.secs}secs"

    def __repr__(self):
        return f"Clock({self.hrs}hrs, {self.mins}mins, {self.secs}secs)"

# Main Scope
c1 = Clock(23, 3, 3)
c2 = Clock(12, 36, 55)

print(c1 + c2)
print(c1 + 20)
print(20 + c1)
