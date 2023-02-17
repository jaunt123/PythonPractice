x = "string variable"
#how to print the fifth character of the string above(have to remember that 0 represents the first character)
print(x[4])
#how to print the second from the last character of the string x, where the last character is -1
print(x[-3])
#how to get the length of the string x, and print the result
y = len(x)
print(y)
#an alternative way to get the third to last character in the string x (could be used for example when the length is not readily known)
print(x[y-3])
#setting a number for pi
pi = 22/7
#pi in string form, rather than number
pi_str = "22/7"
#how to use .format
print(f"pi value {pi} is determined by: {pi_str}")
print("pi value {0} is determined by: {1}".format(pi,pi_str))
print("pi value {1} is determined by: {1}".format(pi,pi_str))
print("pi value {0} is determined by: {0}".format(pi,pi_str))
print("pi value {0:12.12f} is determined by: {1}".format(pi,pi_str))
#for loops
for i in range(0,12):
    print(f"number is: {i} squared is: {i**2} cubed is: {i**3}")
for i in range(0,12):
    print("number is: {0:2} squared is: {1:3} cubed is: {2:4}".format(i,i**2,i**3))
for i in range(0,12):
    print("number is: {0:<2} squared is: {1:<3} cubed is: {2:<4}".format(i,i**2,i**3))
for i in range(0,12):
    print("number is: {0:>2} squared is: {1:>3} cubed is: {2:>4}".format(i,i**2,i**3))


