high = 1000
low = 1
userInput = input("Please enter a number in range in {0} to {1}".format(low,high))
guess = 1
while True:
    guess = low+(high-low)//2
    varGuess = input("My guess is:" + str(guess) + "should I guess higher or lower. Enter h or l or c if my response is correct")
    if varGuess == "h":
        low = guess + 1
    #    userInput = low
    #    print("The entered number is higher than the upper bound, please enter a number between {0} and {1}".format(low,high))
 #       pass
    elif varGuess == "l":
        high = guess - 1
   #     userInput = high
   #     print("The entered number is lower than the lower bound, please enter a number between {0} and {1}".format(low,high))
    #    pass
    elif varGuess == "c":
        print("I got the guesses in {0} occurrences".format(guess))
        exit()
    else:
        print("Enter h, l, c")
    guess = guess + 1