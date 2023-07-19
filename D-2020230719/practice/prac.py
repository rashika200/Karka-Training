# name="Rashika"
# dic_name={"name":name}
# print(dic_name)


# 


# file=open("/home/rashika/rashika.txt","r")
# print(file.read())
# for line in file:
#     print(line)

# # data=file.read()
# # print(data)

# file=open("/home/rashika/rashika.txt","w")
# file.write("I'm Rashika")
# file.close()
# file=open("/home/rashika/rashika.txt","r")
# print(file.read(7))


file=open("/home/rashika/rashika.txt","a")
file.write("rashika")
file.close()
file=open("/home/rashika/rashika.txt","r")
print(file.read())


file=open("/home/rashika/rashika.txt","r")
for line in file:
   print(line.split())