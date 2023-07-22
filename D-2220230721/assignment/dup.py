dup_value=[1,2,3,2,5,1,5]
value=[]
for i in dup_value:
    if i not in value:
        value.append(i)
print("original_value=",value)

# dup_value=[1,2,3,2,5,1,5]
# original_value=set(dup_value)
# print(original_value)