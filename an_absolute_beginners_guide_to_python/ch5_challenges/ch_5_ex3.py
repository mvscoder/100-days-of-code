# ch_5_ex3 Who's your daddy?

print('\t\t\tWho is your Daddy? A fun way to view a royal lineage')

father_son = {
    "Joseph I (1678-1711)": "Leopold I (1640-1705)",
    "Leopold I (1640-1705)": "Ferdinand III (1608-1657)",
    "Ferdinand III (1608-1657)": "Ferdinand II (1578-1637)",
    "Ferdinand II (1578-1637)": "Charles II of Austria (1540-1590)",
    "Charles II of Austria (1540-1590)": "Ferdinand I (1503-1564)",
    "Ferdinand I (1503-1564)": "Philip I of Castile (1478-1506)",
    "Philip I of Castile (1478-1506)": "Maximillian I (1459-1519)",
    "Maximillian I (1459-1519)": "Frederick III (1415-1493)",
    "Frederick III (1415-1493)": "Ernest, Duke of Austria (1377-1424)",
    "Ernest, Duke of Austria (1377-1424)": "Leopold III (1351-1386)",
    "Leopold III (1351-1386)": "Albert II (1298-1358)",
    "Albert II (1298-1358)": "Albert of Germany (1255-1308)",
    "Albert of Germany (1255-1308)": "Rudolph of Germany (1218-1291)",
    "Rudolph of Germany (1218-1291)": "Not Documented",
}

directory = []

for key in father_son.keys():
    directory.append(key)

choice = ''

while choice != 'q':
    print("\n\t\tWelcome to the Hapsburg directory!")
    print("\n\nYou can do any of the following here:\n[1]View a father son pair\n[2]Add a father son pair"
          "\n[3]Delete a father son pair")
    choice = input("\nEnter a number to select what you would like to do, press 'q' to quit: ")
    if choice == '1':
        print("List of Hapsburg sons in lineage:")
        for i in range(0, len(directory)):
            print("[{}] - {}".format(i + 1, directory[i]))
        view = int(input("\nPlease select the number of the individual"
                         " who you would like to see whom their father is: "))
        view -= 1
        print("\nYou selected {}, their father is {}.".format(directory[view], father_son[directory[view]]))

    if choice == '2':
        print("\nYou'd like to add a father son pair:")
        father = input("\nPlease input the father's name, birth year and death year "
                       "in the \"name (birthyear-deathyear)\" format: ")
        son = input("\nPlease input the son's name, birth year and death year "
                       "in the \"name (birthyear-deathyear)\" format: ")
        directory.append(son)
        father_son[son] = father
        print("\nYour father son pair has been added successfully!")

    if choice == '3':
        print("\nYou'd like to delete a father son pair:")
        for i in range(0, len(directory)):
            print("[{}] - {}".format(i + 1, directory[i]))
        deletion = int(input("\nPlease select the number of the individual"
                   " who you would like delete as a son: "))
        deletion -= deletion
        del father_son[directory[deletion]]
        directory.pop(deletion)

    if choice not in ('123q'):
        print("\nInvalid choice, please choose again")

      #" Please select a number to see who was that Famous "
      #"Hapsburg's father")
