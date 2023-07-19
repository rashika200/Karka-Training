numbers=list(range(1,101))
for i,number in enumerate(numbers):
    if (number%3!=0 and number%5!=0):
        print(number)
    if (number%3==0):
        print("Fizz")
    if (number%5==0):
        print("Buzz")
    if (number%3==0 and number%5==0):
        print("FizzBuzz")
