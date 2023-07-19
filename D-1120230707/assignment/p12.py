quiz=input("are you ready for a quiz?")
print("okay, here it comes!")
correct_ans=0
question=0
ques1=int(input("what is the capital of Alaska?\n\t1) Melbourne\n\t2) Anchorage\n\t3) Juneau\n>"))
if (ques1==3):
    question=question+1
    correct_ans=correct_ans+1
    print("that's right !")
else:
    print("that's incorrect")
ques2=int(input("can you store the value cat in a variable of type int?\n\t1)yes\n\t2)no\n>"))
if (ques2==1):
    question=question+1
    print("sorry, 'cat' is a string.ints can only store numbers.")
else:
    correct_ans=correct_ans+1
    print("can store")
ques3=int(input("what is the result of 9+6/3?\n\t1) 5\n\t2) 11\n\t3) 15/3\n>"))
if (ques3==2):
    question=question+1
    correct_ans=correct_ans+1
    print("that's correct!")
else:
    print("that's incorrect")
print(f"overall,you got{correct_ans} out of {question}.\nThanks for playing!")

