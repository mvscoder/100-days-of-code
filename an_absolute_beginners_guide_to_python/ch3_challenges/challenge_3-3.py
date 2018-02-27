# A random number guessing game, with the number ranging from 1 - 20. The user has 4 guesses

import random

guess = 0
guess_number = 0
number_to_guess = random.randint(1, 20)
play = "Y"

print("We're going to play a game, you try to guess a number between 1 and 20. If you can do it in 4 guesses I'll do something special for you!\n")

while play.upper() != "Q":
	while guess_number < 4:
		print("Number of guesses so far: ", str(guess_number))
		guess = int(input("\nGo ahead an enter a number between 1 and 20, if you don't input a number then you might just break me: "))
	
		if guess == number_to_guess:
			print("Nailed it!")
			print("(╯°□°）╯︵ ┻━┻")
			print("I can't belive that you guessed the number was", number_to_guess, "You obviously cheated.")
			print("\n\n")
			break
		elif guess > number_to_guess:
			print("Too high!")
		else:
			print("Too low!")
		guess_number += 1
	if guess_number == 4:
		print("I can't believe you didn't get it. Worst. Guesses. Ever. The number was", number_to_guess, "\n\n")
	play = input("Would you like quit? If so please hit 'q' and then enter ")
	guess_number = 0
	number_to_guess = random.randint(1, 20)
