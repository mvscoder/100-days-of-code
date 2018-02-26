#Flips a coin 100 times and then reports back the number of heads and tails

import random

number_of_flips = 0
heads = 0
tails = 0
winner = ""

input("We're going to flip a coin 100 times and see whether it's more 'heads' or 'tails', which one do you think it will be?")

while number_of_flips < 100:
	if random.randint(0, 1) == 0:
		heads += 1
	else:
		tails += 1
	number_of_flips += 1

if heads > tails:
	winner = "Heads"
else:
	winner = "Tails"

print("It looks like", winner, "won!", "Heads was flipped", str(heads), "times while Tails was flipped", str(tails), "times")
