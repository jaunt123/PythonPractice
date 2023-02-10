x = "string variable"
print(x[4])
print(x[-3])
y = len(x)
print(y)
print(x[y-3])
pi = 22/7
pi_str = "22/7"
print(f"pi value {pi} is determined by: {pi_str}")
print("pi value {0} is determined by: {1}".format(pi,pi_str))
print("pi value {1} is determined by: {1}".format(pi,pi_str))
print("pi value {0} is determined by: {0}".format(pi,pi_str))
print("pi value {0:12.12f} is determined by: {1}".format(pi,pi_str))
for i in range(0,12):
    print(f"number is: {i} squared is: {i**2} cubed is: {i**3}")
for i in range(0,12):
    print("number is: {0:2} squared is: {1:3} cubed is: {2:4}".format(i,i**2,i**3))
for i in range(0,12):
    print("number is: {0:<2} squared is: {1:<3} cubed is: {2:<4}".format(i,i**2,i**3))
for i in range(0,12):
    print("number is: {0:>2} squared is: {1:>3} cubed is: {2:>4}".format(i,i**2,i**3))


