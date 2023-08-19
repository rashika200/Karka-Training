# n=int(input("enter the number :"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):      
#         print(j,end=" ")
#     print(" ")

# for i in range(1,n):
#     # print("*")
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")
# for a in range(n,0,-1):
#     # print("*")
#     for b in range(a):
#         print("*",end=" ")
#     print(" ")


# for i in range(1,n*2):
#     if i<=n:
#         m=i
#     else:
#         m=(n*2)-i
#     for j in range(m):
#         print("*",end=" ")
#     print(" ")


name=input("enter the sentence :")
longest=name.split()
longest_word=max(longest,key=len)
print(longest_word,"is the longest word")