# ch_4_ex4 Player has to guess the word after guessing 5 letters and getting information as to whether they are in the word

import random

WORDS = ("dragonfruit", "spectacular", "bumblebee", "perfidious", "coriander", "acquifer")

word_selected = random.choice(WORDS)

guess = ""

print("\t\t\t Wheel, of, PYTHON!!!")
print("\nHere's how the game works. I choose a word and you get to ask me what letters are in the word.")
print("\nIf a letter is present, I'll say 'yes', if not, I'll say 'no'")
print("\nOnce your five guesses are made I'll ask you to guess the word!\n")
print("\nThe word is", len(word_selected), "characters long\n")

for i in range(5):
    guess = input("\nWhat letter would you like to guess? (enter the letter, then press enter): ")
    if guess.lower() in word_selected:
        print("Great,", guess, "is in the word.")
    else:
        print("Sorry,", guess, "is not in the word.")

guess = input("\nNow that you've made your guesses what do you think the word is?: ")
if guess == word_selected:
    print("Congratulations, you've got it!")
else:
    print("Sorry, better luck next time!")