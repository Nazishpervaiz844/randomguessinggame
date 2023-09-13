# number guessing game
import random

correct_number = random.randint(1,10)
attempts=10

while attempts > 0:
        guess = int(input("enter a number between 1 an 10"))

            print("you guessed the number")
        
        if guess> correct_number:
            print("too high, try again")
        else:
            print("too low, try again")


          