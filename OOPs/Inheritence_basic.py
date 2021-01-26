
class vehcile:

    name="Neena"

# deriving the class {Inherit}
class vehcile_model(vehcile):

    year=2020

ObjectInherit = vehcile_model()

#accessing the base(parent) class variable
print(ObjectInherit.name)

#inherit class varialb
print(ObjectInherit.year)