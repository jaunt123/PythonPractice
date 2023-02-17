name = input("Please enter the name ")

for i in name:
    print(i)

numbers = "2847:;294,832.424"
separators = ""
for i in numbers:
    if i.isnumeric():
        print(i)

day = "Thursday"
temperature = 26
raining = True
if day == "Saturday" or temperature <27 and not raining:
    print("Go swimming")
elif temperature==26:
    print("Stay indoors")
else:
    print("Take rest")

