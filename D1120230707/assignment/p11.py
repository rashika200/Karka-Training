weight=int(input("please enter your current earth weight:"))
print("I have information for the following planets:\n\t1.\tvenus\t2.\tmars\t3.\tjupiter\n\t4.\tsaturn\t5.\turanus\t6.\tnaptune")
planet=int(input("which planet are you visiting?"))
if (planet==1):
    venus=weight*0.78
    print(f"your weight would be{venus} pounds on that planet")
elif (planet==2):
    mars=weight*0.39
    print(f"your weight would be{mars} pounds on that planet")
elif (planet==3):
    jupiter=weight*2.65
    print(f"your weight would be{jupiter} pounds on that planet")
elif (planet==4):
    saturn=weight*1.17
    print(f"your weight would be{saturn} pounds on that planet")
elif (planet==5):
    uranus=weight*1.05
    print(f"your weight would be{uranus} pounds on that planet")
elif (planet==6):
    neptune=weight*1.23
    print(f"your weight would be{neptune} pounds on that planet")
else:
    print("no data found")