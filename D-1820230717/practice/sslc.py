names=[{"name":"Rashika",
        "place":"paraseri",
        "Hobby":["watching tv","sleeping","listening music"],
        "sslc":{"tamil":98,
                "english":96,
                "maths":98,
                "science":95,
                "social":98}},
        {"name":"sulaebha",
        "place":"panagudi",
        "Hobby":["watching tv","using mobile","listening music"],
        "sslc":{"tamil":98,
                "english":90,
                "maths":98,
                "science":93,
                "social":96}},
        {"name":"devi priya",
        "place":"aralvaimozhi",
        "Hobby":["watching tv","playing dogs","listening music"],
        "sslc":{"tamil":98,
                "english":90,
                "maths":98,
                "science":89,
                "social":95}},
        {"name":"kavish",
        "place":"vadasery",
        "Hobby":["games","bike ride"],
        "sslc":{"tamil":90,
                "english":93,
                "maths":85,
                "science":97,
                "social":82}},
        {"name":"rabin",
        "place":"ramanputhur",
        "Hobby":["youtube","games","watching movies"],
        "sslc":{"tamil":98,
                "english":96,
                "maths":98,
                "science":95,
                "social":98}},
        {"name":"reshma",
        "place":"marthandam",
        "Hobby":["cooking","gardening","listening music"],
        "sslc":{"tamil":96,
                "english":94,
                "maths":88,
                "science":90,
                "social":92}},
        {"name":"aswin kumar",
        "place":"nagercoil",
        "Hobby":["watching movies","cooking","playing cricket"],
        "sslc":{"tamil":99,
                "english":97,
                "maths":98,
                "science":94,
                "social":98}}]
for name in names:
    # print(name["sslc"])
    tamil=(name["sslc"]["tamil"])
    english=(name["sslc"]["english"])
    maths=(name["sslc"]["maths"])
    science=(name["sslc"]["science"])
    social=(name["sslc"]["social"])
    total=tamil+english+maths+science+social
    print(total)
    
#     average=total/5
#     print(average)

#     if average>90:
#         print(name,"they are eligible for maths biology")
#     if average>80 and average<=90:
#         print(name,"they are eligible for computer science")
#     if average>75 and average<=80 and maths<98:
#         print(name,"they are eligible for maths biology")
#     if average>70 and maths>98:
#         print(name,"they are eligible for computer science")
    






