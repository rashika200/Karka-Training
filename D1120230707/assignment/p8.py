name=input("hey, what's your name?")
age=int(input(f"ok,{name},how old are you?"))
if age<16:
    print(f"you can't drive,{name}")
if age<18:
    print(f"you can't vote,{name}")
if age<25:
    print(f"you can't rent a car,{name}")
if age>=25:
    print(f"you can't do anything that's legally,{name}")
