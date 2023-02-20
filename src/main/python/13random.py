import random
highest = 1000
lowest = 1
result = random.randint(lowest,highest)
print(result)
guess = int(input("Please try to guess the number:"))
while True:
    if guess == result:
        print("exit process")
        break
    elif guess > result:
        highest = guess
        guess = int(input("The entered guess is larger than result, please guess a smaller number between: {0} and {1}".format(lowest,highest)))
        continue
    elif guess < result:
        lowest = guess
        guess = int(input("The entered guess is larger than result, please guess a smaller number between: {0} and {1}".format(lowest,highest)))
        continue