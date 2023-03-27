x = int(input(" please enter number of Emoje that you want: "))
for i in range(1,x):
    for j in range(x,x+i):
        print("\U0001f600", end="")
    print()