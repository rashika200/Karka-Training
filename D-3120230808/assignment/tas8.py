s="abcabcbb"
a=list(s)
# print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(len(b))