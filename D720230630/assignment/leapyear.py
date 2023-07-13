
year=int(input("which is a leapyear"))
if ((year%4==0) and
    (year%100!=0) or
    (year%400==0)):
        print("given number is a leapyear")
else:
        print("given number is not a leapyear")       