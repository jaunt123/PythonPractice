vlist = ["drive", "screen", "keyboard", "RAM"]
for parts in vlist:
    print(parts)



print(vlist[3])
print(vlist[-1])
print(vlist[1:3])

booklist = ["Harry Potter", "Divergent", "Percy Jackson"]
for i in booklist:
    print(i)
    if "a" in i or "e" in i or "i" in i or "o" in i or "u" in i:
        print("the vowel is present")
    else:
        print("the vowel is not found")

