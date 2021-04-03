import random
print("Number Guessing Game")
num=random.randint(1,9)
guess = input("Enter your guess (between 1 and 9):")
chance=0
while chance<5:
    guess=int(input("Enter your guess: "))
    if guess == num :
        print("Congratulations !! You won.")
        break
    else :
        print("Try again!")
    chance= chance+1

if chance==5 :
    print("You loose! the number is", num)      



