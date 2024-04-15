place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("do you light a torch, or proceed in the dark?")
    if action == "light a torch":
        print("you light a torch and see a cave full of spiders, time to leave!")
    elif action == "proceed in the dark":
        print("game over")
else:
    pass