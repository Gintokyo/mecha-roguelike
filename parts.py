class Part:
    def __init__(self, name, part_type, stats):
        self.name = name
        self.part_type = part_type
        self.stats = stats

    def __str__(self):
        return f"{self.name} ({self.part_type}) -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items())

    # Changing stats
    # self is needed for the function but will be called automatically by Python
    # Part.apply_to(Mech) == heavy_chassis.apply_to(heavy_chassis, my_mech)
    def apply_to(self, mech):
        for k, v in self.stats.items():
            mech.stats[k] += v
            return mech.stats