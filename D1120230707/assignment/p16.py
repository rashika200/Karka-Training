gender=input("what is your gender (M or F):")
name1=input("enter first name:")
name2=input("enter last name:")
age=int(input("enter your age:"))
name = (name1 +' ' +name2)
if (gender=="f" and age>=20):
    married=input(f"are you married,{name1} (y or n)?")
    if (married=="y"):
        print(f"then I shall call you Mrs.{name}")
    else:
        print(f"then i shall call you Ms.{name}")
    
if (gender=="f" and age<20):
    print(f"then i call you {name}")
if (gender=="m" and age>=20):
    print(f"then i call you Mr.{name}")

