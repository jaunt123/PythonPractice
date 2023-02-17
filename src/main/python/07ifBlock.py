name = input("Please enter the name:")
#age = int(input("Please enter the age, {0}?".format(name)))
age = None # int(input("Please enter the age, {0}?".format(name)))
if  age is not None:
    if age >= 18 and age is not None:
        print("You are allowed to vote")
    else:
        print("Please come back after {0} years".format(18-age))




name = input("Please enter the name:")
age = int(input("Please enter the age, {0}?".format(name)))
#age = None # int(input("Please enter the age, {0}?".format(name)))
if age is not None:
    if age > 18:
        print("You are allowed to vote")
    elif age == 18:
        print("Congrats you are allowed to vote this year!")
    else:
        print("Please come back after {0} years".format(18-age))
if name:
    print("True")
else:
    print("False")

if True:
    print("Statement is true")
else:
    print("Statement is false")

day = "Friday"
temperature = 27
raining = False
if (day == "Saturday" and temperature <27 or not raining):
    print("Go swimming")
else:
    print("Take rest")

parrot = "Norwegian blue"
letter = input("Please enter the letter to be checked:")
if letter.casefold() in parrot.casefold() and len(letter)>0:
    print("Letter found")
else:
    print("Letter not found")





