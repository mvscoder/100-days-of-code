# ch05_ex_1 - Populate and print a list of words in random order

import random


print("\t\t\t Random word order bot!")

new_word = "a"
word_list = []
list_index = 0

while new_word.lower() != 'q':
    new_word = input("\nPlease enter a new word to add to the list, \nor press 'q' then enter to quit: ") 
    if new_word.lower() == 'q':
        break
    else:
        word_list.append(new_word)
    
for item in range(0, len(word_list)):
    choice = random.randint(0, len(word_list) - 1)
    print(word_list[choice])
    word_list.pop(choice)