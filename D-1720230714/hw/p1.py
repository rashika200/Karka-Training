names=[{"name":"Rashika",
        "age":21,
        "place":"paraseri"}, 
        {"name":"Devi priya",
         "age":21,
         "place":"aralvaimozhi"},
        {"name":"Vimala",
         "age":22,
         "place":"villukuri"},
        {"name":"Sureca",
         "age":21,
         "place":"thoothukudi"},
        {"name":"Sujin bouncy",
         "age":23,
         "place":"irachakulam"}]
for i,name in enumerate(names): 
     print (f"I am",name["name"],",I'm",name["age"],"years old,and I'm from",name["place"])





names=[{"name":"Rashika",
        "age":21,
        "pl;ace":"paraseri"}, 
        {"name":"Devi priya",
        "age":21,
        "place":"aralvaimozhi"},
        {"name":"Vimala",
        "age":22,
        "place":"villukuri"},
        {"name":"Sureca",
        "age":21,
        "place":"thoothukudi"},
        {"name":"Sujin bouncy",
        "age":23,
        "place":"irachakulam"}]
for name in names:
    if (name["age"])>21: 
        print (f"I am",name["name"],",I'm",name["age"],"years old,and I'm from",name["place"])
        