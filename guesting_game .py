# guesting game between 1 and 10

#num = int(input(" Guess number between 1 and 10: "))
while True:
    num = int(input(" Guess number between 1 and 10: "))
    if num >= 1 and num <=4:
        print("Too low, try again!")
    elif num >= 6 and num <= 10:
        print("Too high, try again!")
    else:
        print("you guessed it, you won!")
    x = input("Do you want to continou or exit(y/n): ")
    if x == 'y':
        continue
    else:
        break
