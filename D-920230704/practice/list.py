# list iterations
fruits=["apple","orange","grapes","mango","straberry","pineapple","lichi","banana"]
for i,fruit in enumerate(fruits):
    if (i<=3):
        print(fruit)
    else:
        break


fruits=["apple","orange","grapes","mango","straberry"]
fruit=fruits[2:4]
print(fruit)



fruits=["apple","orange","grapes","mango","straberry"]
fruit=len(fruits)
print(fruit)



fruits=["mango","orange","apple","pineapple","straberry","banana","lichi","grapes"]
for i,fruit in enumerate(fruits):
    if(i<=5):
        continue
    else:
        print(fruit)



fruits=["mango","orange","apple","pineapple","straberry","banana"]
for i, fruit in enumerate(fruits):
    if(i+3)%6==0:
        print(fruit)



# dictionary
name={"rashika":21,
      "vijay":26,
      "ranjith":24}
print (name["rashika"])



# set
# fruits={"mango","orange","apple","pineapple","straberry","banana"}
# print(fruits[2:3])




# tuple
fruits=("mango","orange","apple","pineapple","straberry","banana")
print(fruits[1:3])



fruits=("mango","orange","apple","pineapple","straberry","banana")
fruit=len(fruits)
print(fruit)




letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
for i, letter in enumerate(letters):
    if ((i+1)%4==0):
        print(letter)




letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
for i, letter in enumerate(letters):
    if ((i+1)%2==0):
        print(letter)




letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
for i, letter in enumerate(letters):
    if (i<=7):
        continue
    else:
        print(letter)




letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
for i, letter in enumerate(letters):
    if (i<=3):
        print(letter)
    else:
        break




letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
letter=letters[0]
print(letter)