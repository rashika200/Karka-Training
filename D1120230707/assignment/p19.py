print("I'm thinking of a number between 1-100. You have 7 guesses.")
number=int(input("enter the number"))
guess1=int(input ("enter guess1"))
if (guess1<number):
    print("you are too low.")
elif (guess1>number):
    print("you are too high")
elif (guess1==number):
    print("you guess it")
    exit()

guess2=int(input("enter guess2"))
if (guess2<number):
    print("you are too low.")
elif (guess2>number):
    print("you are too high")
elif (guess2==number):
    print("you guess it")
    exit()


guess3=int(input("enter guess3"))
if (guess3<number):
    print("you are too low.")
elif (guess3>number):
    print("you are too high")
elif (guess3==number):
    print("you guess it")
    exit()


guess4=int(input("enter guess4"))
if (guess4<number):
    print("you are too low.")
elif (guess4>number):
    print("you are too high")
elif (guess4==number):
    print("you guess it")
    exit()



guess5=int(input("enter guess5"))
if (guess5<number):
    print("you are too low.")
elif (guess5>number):
    print("you are too high")
elif (guess5==number):
    print("you guess it")
    exit()



guess6=int(input("enter guess6"))
if (guess6<number):
    print("you are too low.")
elif (guess6>number):
    print("you are too high")
elif (guess6==number):
    print("you guess it")
    exit()


guess7=int(input("enter guess7"))
if (guess7<number):
    print("you are too low.")
elif (guess7>number):
    print("you are too high")
elif (guess7==number):
    print("you guess it")
    exit()

else:
    print("sorry,you didn't guess it in 7 tries. You lose.")
    

