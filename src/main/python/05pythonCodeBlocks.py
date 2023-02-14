a = "number is even"
b = "number is odd"
try:
    for i in range (1,100):
        print(i)
        try:
            if (i%0 == 0):
                print("after first loop:" + a)
                for j in range (1,3):
                    print("after second loop:" + a)
            else:
                print(b)
        except Exception as E:
            print("inner Exception is: " + str(E))
    print("*" *80)
except Exception as E:
    print("error is:" + E)
finally:
    print("final line is:")