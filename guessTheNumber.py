## This is a guess the number game.
import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess six times.
for guessTaken in range(1, 7):
  print('Take a guess.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high')
  else:
    break #condition is the correct guess!

if guess == secretNumber:
    print('Good job! you guess my number in ' +str(guessTaken) + ' guesses!')
else:
  print('Nope, The number I was thinking was ' +str(secretNumber))
