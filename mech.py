class Mech:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "HP": 100,
            "ATK": 10,
            "DEF": 5
        }

    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}:{v}" for k, v in self.stats.items())