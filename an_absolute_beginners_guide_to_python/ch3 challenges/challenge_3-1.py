#Generates a fortune from a fortune cookie using a randomized 1-5 selection until the user exits.

import random

print("\t\t\t ***Mysterious Fortune Cookie***")

choice = "Y"


while choice.upper() == "Y":
	fortune_number = random.randint(1, 5)
	print("The mysterious fortune cookie crumbles and says:")

	if fortune_number == 1:
		print("This is the day you should buy lottery tickets")
	elif fortune_number == 2:
		print("A great day to get some fresh air, go outside more")
	elif fortune_number == 3:
		print("This a neutral day, you should avoid making decisions on anything more complicated than what to have for lunch")
	elif fortune_number == 4:
		print("Stick with your wife")
	else:
		print("We're truly so sorry. You don't know what for yet, but damn...")

	choice = input("Hit 'y' and then enter for another one, any other key and then enter to quit :")

input("Thanks for having your fortune read!")	