parrot = "Norwegian blue"
for i in parrot:
    print(i)

numbers = "9,223;372:036 854,755;807"
separators = ""
for i in numbers:
    if not i.isnumeric():
        separators=separators+i

print(separators)
