user_input = int(input("enter number : "))
for i in range(user_input):
    for j in range(((user_input-1)-i)):
        print(" ",end='  ')
    for j in range(i):
        print("*",end="  ")
    for j in range(i+1):
        print("*",end="  ")
    print()