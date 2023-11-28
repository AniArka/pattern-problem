user_input = int(input("enter number : "))
for i in range(user_input):
    for j in range(i,user_input):
        print(" ",end='  ')
    for j in range(i+1):
        print("*",end='  ')
    print()