print("WELCOME TO MITCHELL'S TINY ADVENTURE!")
place=input("you are in a creepy house! Would you like to go upstairs or into the kitchen\n>")
if (place=="kitchen"):
    kitchen=input("there is a long countertop with dirty dishes everywhere. Off to one side there is, as you'd expect, a refrigerator. You say open the refrigerator or look in a cabinet.\n>")
    if (kitchen=="refrigerator"):
        print("Inside the refrigerator you see food and stuff. It looks pretty nasty.")
        refrigerator=input("Would you like to eat some of the food? (yes or no)\n>")
        if (refrigerator=="yes"):
            print("enjoy your food")
        elif (refrigerator=="no"):
            print("you die of starvation....eventually")
    elif (kitchen=="cabinet"):
        print("there is a snacks inside it.")
        cabinet=input("Would you like to eat (yes or no)\n>")
        if (cabinet=="yes"):
            print("enjoy your snacks")
        elif (cabinet=="no"):
            print("you die of starvation...eventually")
    


elif (place=="upstairs"):
    upstairs=input("there is a bed room and store room. You would like to go bedroom or store room")
    if (upstairs=="bedroom"):
        print("there is a dust. ")
        bedroom=input("would you clan it(yes or no)\n>")
        if (bedroom=="yes"):
            print("go and clean the room")
        elif (bedroom=="no"):
            print("do later")
    elif (upstairs=="storeroom"):
        print("there is a empty boxes.")
        storeroom=input("Would you like to clean(yes or no)\n>")
        if (storeroom=="yes"):
            print("store empty boxes in the room")
        elif (storeroom=="no"):
            print("do it later")
else:
    print("do any work")



