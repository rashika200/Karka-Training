print("Two Questions!\nThink of an object, and I'll try to guess it.")
ques1=input("question 1) Is it animal, vegetable, or mineral?\n>")
ques2=input("question2) Is it bigger than a breadbox?\n>")
if (ques1=="animal" and ques2=="yes"):
    print("My guess is that you are thinking of mouse.\nI would ask you I'm right, but I don't actually care.")
elif (ques1=="vegetable" and ques2=="yes"):
    print("My guess is that you are thinking of watermelon.\nI would ask you I'm right, but I don't actually care.")
elif (ques1=="mineral" and ques2=="yes"):
    print("My guess is that you are thinking of camaro.\nI would ask you I'm right, but I don't actually care.")
elif (ques1=="animal" and ques2=="no"):
    print("My guess is that you are thinking of squirrel.\nI would ask you I'm right, but I don't actually care.")
elif (ques1=="vegetable" and ques2=="no"):
    print("My guess is that you are thinking of carrot.\nI would ask you I'm right, but I don't actually care.")
elif (ques1=="mineral" and ques2=="no"):
    print("My guess is that you are thinking of paper clip.\nI would ask you I'm right, but I don't actually care.")
else:
    print("no data found")