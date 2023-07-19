# names=["Sulaebha","Rashika","Kavish","Devi Priya","Rabin","Reshma","Aswin Kumar"]
# for i, name in enumerate(names):
    # print(name)




names=[{"name":"Rashika",
        "place":"paraseri",
        "Hobby":["watching tv","sleeping","listening music"]},
        {"name":"sulaebha",
        "place":"panagudi",
        "Hobby":["watching tv","using mobile","listening music"]},
        {"name":"devi priya",
        "place":"aralvaimozhi",
        "Hobby":["watching tv","playing dogs","listening music"]},
        {"name":"kavish",
        "place":"vadasery",
        "Hobby":["games","bike ride"]},
        {"name":"rabin",
        "place":"ramanputhur",
        "Hobby":["youtube","games","watching movies"]},
        {"name":"reshma",
        "place":"marthandam",
        "Hobby":["cooking","gardening","listening music"]},
        {"name":"aswin kumar",
        "place":"nagercoil",
        "Hobby":["watching movies","cooking","playing cricket"]}]
for i, name in enumerate(names):
    print(name)


names={"name":"rashika",
       "place":"paraseri"}
print(f"I'm from",names["place"])



print(names[3]["Hobby"])
for hobby in names[3]["Hobby"]:
    print(hobby)




marks={"tamil":100,
       "english":97,
       "maths":97,
       "science":95,
       "social":98}
print(marks.items())
print(marks.values())
print(marks.keys())