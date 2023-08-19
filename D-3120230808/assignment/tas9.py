number=[[1,2,3,[4,5]],[6,7,[8,9]],[10,[11,12,13]]]
num=[]
num1=[]
for i in number:
    for j in i:
        name=type(j)
        # print(name)
        if name==list:
            num.append(j)
        if name==int:
            num1.append(j)
# print(num1,end=" ")
output=[]
for a in num:
    for b in a:
        output.append(b)
# print(output,end=" ")

value=num1+output
value.sort()
# print(value) 
for n in value:
    print(n,end=" ")     

