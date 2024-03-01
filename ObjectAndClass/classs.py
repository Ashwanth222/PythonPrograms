class Parrot:
    name = ""
    age = 0

parrot1 = Parrot()

parrot1.name = "name1"
parrot1.age = 10

parrot2 = Parrot()

parrot2.name = "name2"
parrot2.age = 20

print(f"parrot name is {parrot1.name} and age is {parrot1.age}")
print(f"parrot name is {parrot2.name} and age is {parrot2.age}")


#

class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
