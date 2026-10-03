class Mech:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "MAX_HP": 100,
            "HP": 100,
            "ATK": 10,
            "DEF": 5
        }
        self.parts = []

    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items() if k != 'MAX_HP') + "\nParts: " + " ".join(f"{p.name} ({p.part_type})" for p in self.parts)

    # Dealing damage
    def take_damage(self, amount):
        self.stats["HP"] -= amount
        if self.stats["HP"] < 0:
            self.stats["HP"] = 0
    # Healing damage
    def heal(self, amount):
        self.stats["HP"] += amount
        if self.stats["HP"] > self.stats["MAX_HP"]:
            self.stats["HP"] = self.stats["MAX_HP"]

    # Equipping parts
    # self refers to what appears before the function i.e. my_mech.equip_part -> my_mech is self
    def equip_part(self, part):
        for p in self.parts:
            if p.part_type == part.part_type:
                print(f"{part.part_type} already equipped")
                # The break here and the else out of the for loop allows p.part_type to check after the first argument only i.e. if we have 'Body', 'Arm' it will not stop at 'Body' and then finish the loop.
                break
        else:
            part.apply_to(self)
            self.parts.append(part)