from mech import Mech
from parts import Part

my_mech = Mech("Atlas")

print(my_mech.name)
print(my_mech)

heavy_chassis = Part("Heavy Chassis", "Body", {"HP": 20, "DEF": 10})

print(heavy_chassis)
# Code a better output
print(heavy_chassis.apply_to(my_mech))