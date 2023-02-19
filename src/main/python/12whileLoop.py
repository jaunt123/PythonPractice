i = 0
while i <=10:
    print (i)
   # i = i+1
    i += 1
    break

available_exits = ["North", "South", "East", "West"]
choose_exit = ""
while choose_exit not in available_exits:
    choose_exit = input("Please enter the direction:")
    if choose_exit.casefold() == "quit".casefold():
        print("game over")
        break

