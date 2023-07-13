# area of triangle using Heron's formula
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
def semi_perimeter(a,b,c):
    s=(a+b+c)/2
    return s
semi_perimeter=semi_perimeter(a,b,c)
print("semi_perimeter=",semi_perimeter)


s=semi_perimeter
def area(s,a,b,c):
    area=(s*(s-a)*(s-b)*(s-c))**1/2
    return area
area=area(s,a,b,c)
print("area of triangle=",area)




# area of a square
a=int(input("enter the value"))
def area(a):
    area=a**2
    return area
area=area(a)
print("area of square=",area)



# area of rectangle
length=int(input("enter the value"))
breadth=int(input("enter the value"))
def area(length,breadth):
    area=length*breadth
    return area
area=area(length,breadth)
print("area of rectangle=",area)




# area of circle
radius=int(input("enter the value"))
def area(radius):
    area=3.14*radius**2
    return area
area=area(radius)
print("area of circle=",area)




# area of trapezium
a=int(input("enter the value"))
b=int(input("enter the value"))
h=int(input("enter the value"))
def area(a,b,h):
    area=(1/2)*(a+b)*h
    return area
area=area(a,b,h)
print("area of trapezium=",area)