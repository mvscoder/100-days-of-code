# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# the player has to guess the original word


# import the random module
import random

# Words data set
WORDS = ("dogs", "dicitionary", "parameter", "argument", "Javascript", "frameword")

# grab one of the words from WORDS
choice = random.choice(WORDS)

correct = choice

#create empty string to fill with jumbled word
jumbled = ""

#loop to create the jumbled word

while choice:
	letter_to_add = random.randrange(len(choice))
	jumbled += choice[letter_to_add]
	choice = choice[:letter_to_add] + choice[(letter_to_add)]

print("\t\t\tWORD JUMBLER!")
print("\n\nWelcome to word jumble, can you identify the jumbled word?")
print(jumbled)
print(word)
