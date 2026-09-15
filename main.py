from mech import Mech

my_mech = Mech("Atlas")

print(my_mech.name)
print(my_mech)
my_mech.take_damage(12)
print(my_mech)

my_mech.take_damage(101)
print(my_mech)