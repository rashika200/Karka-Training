print("x   y")
print("-"*12)
x=list(range(-10,10,1))
for i, x in enumerate(x):
    x=x-0.5
    y=x**2
    print(x, y)