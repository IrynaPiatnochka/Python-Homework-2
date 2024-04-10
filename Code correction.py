#Code correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else: 
    place == "cave"
    print("You find a hidden treasure!")



#Providing outcome to the story

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else: 
    place == "cave"
    print("You find a hidden treasure!")
    answer = input("Do you want to light a torch? 'yes' or 'no' ")
    if answer == 'yes':
        print("You can use two stones to make a fire spark for your torch.")
    else:
        print("Proceed in the dark.")