# n=5
# for i in range(n):
#     # print(n)
#     for a in range(n):
#         # end=" "
#         print("*",end=" ")
#     print("")
    

# n=5
# num=1
# for i in range(n):
#     for a in range(n):
#         print(num,end=" ")
#         num+=1
#     print("")

# n=5
# for i in range(1,(n*n)+1):
#     print(i,end=" ")
#     if i%n==0:
#         print("\n")

n=5
for i in range(n*n,0,-1):
    # print(i,end=" ")
    if i%n==0:
        print("\n")
    print(i,end=" ")

