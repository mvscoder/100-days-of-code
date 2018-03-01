# Chapter 5 exercise 2 - RPG Character Creator

att_points = {
    "s": 0,
    "h": 0,
    "w": 0,
    "d": 0,
}

att_short = {
    's': 'Strength',
    'h': 'Health',
    'w': 'Wisdom',
    'd': 'Dexterity',
}

points = 30
point_choice = 0
att_choice = ""
confirm = "no"
confirm_points = 'n'
operator = ''

print("\t\t\t RPG Character Creator")
print("\nYou'll use this program to create a new character")
print("for an RPG, the character has 4 attributes: strength,")
print("health, wisdom, and dexterity. You have 30 points to")
print("distribute between these attributes.")

while confirm != 'y':
    print("\n\nThis is how you've spent your attribute points so far:")
    print("Strength: ", att_points["s"])
    print("Health:   ", att_points["h"])
    print("Wisdom:   ", att_points["w"])
    print("Dexterity:", att_points["d"])
    print("You have", points, "left to spend.")

    att_choice = input("\nTo change points for an attribute, input the first letter of the attribute and then enter:"
                       "\npress \"q\" then enter to quit ")
    confirm_points = 'n'
    if att_choice.lower() in "shwd":
        while confirm_points.lower() != 'y':
            print("You've selected", att_short[att_choice])
            print("You've spent", att_points[att_choice], "on this attribute and have", points, "left to spend.")
            change = int(input('Please enter how many points you\'d like to increase or decrease {} by, use a negative '
                               'sign to decrease points: '.format(att_short[att_choice])))
            if change not in range(-30, 30):
                print("\n\nThat's not a valid input, please try again\n\n")
            if att_points[att_choice] + change < 0:
                print("No attribute can be negative, please try again.")
            elif points - change < 0:
                print("You're tryint go assign too many points. You are only allowed 30 and "
                      "you have overspent by {}".format(30 - points - change))
            else:
                att_points[att_choice] += change
                points -= change
                print("\n\n{} is now equal to {}. You have {} points remaining.".format(att_short[att_choice],
                                                                                        att_points[att_choice], points))
                confirm_points = input("If you're happy with your changes, please press \'y\' then enter, "
                                       "to make additional changes press 'enter'.")
    if att_choice == 'q' and points == 0:
        confirm = input("Are you sure you'd like to quit? You have spent all of your points. Press 'y' to quit:")
    elif att_choice == 'q' and points > 0:
        confirm = input("Are you sure you'd like to quit? You have {} points left to spend! "
                        "Press 'y' to quit:".format(points))

print("\n\nCharacter creation complete.")