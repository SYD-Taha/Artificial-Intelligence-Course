#Number Guessing Game

import random

number = random.randint(1,10)
guess = 0

while(guess != number):
  guess = int(input("Guess a number between 1 and 10: "))

  if (guess == number):
    print("You guessed the correct number")
  else:
    print("Guess Again")
