

class Compound(object):
    def __init__(self, formula: str, name: str):
        self.formula = formula
        self.name = name

    def __add__(self, other):
        if not isinstance(other, Compound):
            raise TypeError("Addition can only be performed between Compound types.")

        print(f"Adding {self.name} ({self.formula}) + {other.name} ({other.formula})")
        new_name = f"{self.name}-{other.name}"
        new_formula = f"{self.formula}+{other.formula}"
        return Compound(new_name, new_formula)

    def __str__(self):
        return f"{self.formula}: {self.name}"

    def __repr__(self):
        return f"Compound({self.formula}, {self.name})"

c1 = Compound("HCl", "Hydrochloric Acid")
c2 = Compound("H2O", "Water")

print(c1 + c2)
