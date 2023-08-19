number_stock=int(input("enter the number"))
# cost_stock=list(input("enter the cost"))
value=[]
for i in range(0,number_stock):
    cost_stock=list(input("enter the cost "))
    value.append(cost_stock)
min=value[0]
max=0
for i in range(0,len(value)):
    if value[i]<min:
        min=value[i]
        minimum=i
        # print(minimum)
        for j in range(i+1,len(value)):
            if j>max:
                # max=value[j]
                maximum=j
                # print(maximum)

print(minimum,maximum)
# print("profit is",maximum-minimum)




