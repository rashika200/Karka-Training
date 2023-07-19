# height=float(input("enter your height in m:"))
# weight=int(input("enter your weight in kg:"))
def BMI(weight,height):
    BMI=weight/(height**2)
    return BMI
# BMI=BMI(weight,height)
print("your BMI is",BMI)