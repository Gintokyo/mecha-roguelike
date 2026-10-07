from mech import Mech
from parts import Part

my_mech = Mech("Atlas")

print(my_mech.name)
print(my_mech)

heavy_chassis = Part("Heavy Chassis", "Body", {"MAX_HP": 20, "DEF": 10})
light_chassis = Part("Light Chassis", "Body", {"MAX_HP": 30, "DEF": 5})
heavy_arms = Part("Heavy Arms", "Arms", {"ATK": 30})

print(heavy_chassis)
my_mech.equip_part(heavy_chassis)

part_pool = [
    heavy_chassis,
    light_chassis,
    heavy_arms,
]

for p in my_mech.parts:
    if p.my_mech.parts in my_mech.parts:
        print(f"{my_mech.parts} already equipped")
        # The break here and the else out of the for loop allows p.part_type to check after the first argument only i.e. if we have 'Body', 'Arm' it will not stop at 'Body' and then finish the loop.
        break
else:
    my_mech.equip_part(p)