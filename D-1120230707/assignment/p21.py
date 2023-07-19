import p7
height=float(input("your height in m: "))
weight=int(input("your weight in kg: "))
BMI=p7.BMI(weight,height)
print(BMI)
if (BMI<18.5):
    print("BMI category: under weight")
elif (BMI>=18.5 and BMI<=24.9):
    print("BMI catergory : normal weight")
elif (BMI>=25.0 and BMI<=29.9):
    print("BMI category : over weight")
elif (BMI>=30.0):
    print("BMI category: obese")
else:
    print("no value found")
