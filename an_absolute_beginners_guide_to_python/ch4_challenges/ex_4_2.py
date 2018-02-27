# Gets a message from the user and then reverses it

print("\t\t\tWelcome to the reversomatic!\n\n")

message = input("Please input the message you would like reversed: ")
new_message = ""

for letter in range(len(message) - 1, -1, -1):
	new_message += message[letter]

print(new_message)
