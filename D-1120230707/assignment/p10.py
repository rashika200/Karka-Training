name=input("hey, what's your name? (sorry, I keep forgetting.)")
age=int(input(f"ok, {name}, how old are you?"))
def eligible(age):
    if age<16:
        return (f"you can't drive,{name}")
    elif (age>=16 and age<=17):
        return (f"you can drive but not vote,{name}")
    elif (age>=18 and age<=21):
        return (f"you can vote but not rent a car,{name}")
    elif (age>=25):
        return (f"you can do pretty much anything,{name}")
    else:
        return ("no value found")
age1=eligible(age)
print(age1)