c = "number is odd"
d = "number is even"
for l in range(101):
        print(l)
        try:
            if l%2 == 0:
                print(d)
            else:
                print(c)
        except Exception as E:
            print("Exception is" + str(E))
print("*"*80)





