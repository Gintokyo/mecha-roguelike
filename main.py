from mech import Mech
from parts import Part

my_mech = Mech("Atlas")

print(my_mech.name)
print(my_mech)

heavy_chassis = Part("Heavy Chassis", "Body", {"MAX_HP": 20, "DEF": 10})

print(heavy_chassis)
# Code a better output
heavy_chassis.apply_to(my_mech)
heavy_chassis.apply_to(my_mech)
print(my_mech)