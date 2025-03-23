import random
target=random.randint(1,100)
while True:
    userch=(input("Guess the number or QUIT(Q): "))
    if(userch=="Q"):
        break
    userch=int(userch)
    if(userch==target):
        print("SUCCESS: YOU GUESS CORRECTLY")
        break
    elif(userch<target):
        print("Your number was small : Take a bigger guess")
    else:
         print("Your number was big : Take a smaller guess")

print("----GAME OVER-----")    