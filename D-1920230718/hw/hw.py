items=[{"name":"apple","category":"fruits"},
            {"name":"carrot","category":"vegetables"},
            {"name":"banana","category":"fruits"},
            {"name":"broccoli","category":"vegetables"}]

fruits=[]
vegetables=[]
for i in items:
    if i["category"]=="fruits":
        fruits.append(i["name"])
    if i["category"]=="vegetables":
        vegetables.append(i["name"])

# print(fruits)
# print(vegetables)
dict_fruits={"fruits":fruits,"vegetables":vegetables}
print(dict_fruits)

