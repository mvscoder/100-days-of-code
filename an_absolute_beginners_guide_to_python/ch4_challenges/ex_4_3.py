# ch_4_ex3_word_jumble_improvement

import random

WORDS = ("dragonfruit", "spectacular", "bumblebee", "perfidious", "coriander", "acquifer")

word_selected = random.choice(WORDS)

hint_pos = 0
stored_word = word_selected
user_choice = "n"
guess = ""
jumbled_word = ""

while len(word_selected) > 0:
    letter_choice = random.randint(0, len(word_selected) - 1)
    jumbled_word += word_selected[letter_choice]
    word_selected = word_selected[:letter_choice] + word_selected[letter_choice + 1: len(word_selected)]

print(jumbled_word)

print("\t\t\t Word Jumble, improved!")
while guess != stored_word:
    print("\nYour jumbled word is...: ", jumbled_word)
    guess = input("Please input your guess as to what the jumbled_word is or press 'h' then enter for a hint: " )
    if guess.lower() == 'h':
        hint_pos += 1
        print("\nYou've asked for", hint_pos, "hints so far.")
        print("\nThe first", hint_pos, "letters in the word are:", stored_word[0: hint_pos])

print("\nYay, you guessed the word correctly!")
if hint_pos > 0:
    print("You needed", hint_pos, "hints to guess the word.")
    if hint_pos > 3:
        print("You are really bad at this.")