import random as rd
num=rd.randint(0,20)

guess = input("Guess a number between 0 & 20:\n")
 
guess = int(guess)

if guess < num:
    print (" Oops! your guess is too low\n")

elif guess > num:
    print (" Oops! your guess is too high\n")
        
else :
    print (" Congratulations! you have made a right guess\n")

print("Hey,",num, "is the random generated number")
