#Number Guessing in Python Programming  --- Coding Desk

import random
n = random.randrange(100)
guess_number = int(input("Enter any number: "))
while n!= guess_number:
    if guess_number < n:
        print("Number is too low!")
        guess_number = int(input("Enter number again: "))
    elif guess_number > n:
        print("Number is too high!")
        guess_number = int(input("Enter number again: "))
    else:
      break
print("Hey! you guessed it right!!")
