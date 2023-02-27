#strings are immutableabc = "hello"
string2 = abc
print(string2)
print(abc)
print(id(string2))
print(id(abc))
abc = abc+abc
print(string2)
print(abc)
print(id(string2))
print(id(abc))



#lists are mutable
list1 = ["monitor", "RAM", "keyboard"]
list2 = list1
print(list1)
print(id(list1))
print(list2)
print(id(list2))
list1 += ["mouse"]
print(list1)
print(id(list1))
print(list2)
print(id(list2))