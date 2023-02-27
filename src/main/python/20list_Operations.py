list1 = ["fruits", "vegetables", "nuts"]
list2 = []
for i in list1:
    print(i)
    list2.append(i)
#Use append to add elements to a list


print(list2)


for i in list2:
    print(i)
    list1.remove(i)
print(list1)
#Use remove to eliminate elements from a list
