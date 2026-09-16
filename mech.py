class Mech:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "MAX_HP": 100,
            "HP": 100,
            "ATK": 10,
            "DEF": 5
        }

    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items() if k != 'MAX_HP')

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