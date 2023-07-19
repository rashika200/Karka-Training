my_resume={"name":"P.Rashika",
           "email":"perumalrashika@gmail.com",
           "mobile no":8903917992,
           "soft skill":["work ethic","willingness to learn"],
           "hard skill":["writing","presentation"],
           "educational qualification":[{"qualification":"sslc","school name":"SRMS","passed_out_year":2017,"percentage":96.5},
                                        {"qualification":"hsc","school name":"ACGHSS","passed_out_year":2019,"percentage":60},
                                        {"qualification":"B.E","college name":"LJCET","passed_out_year":2023,"cgpa":7.5}],
            "project":"SOFTWARE PRIVACY PROTECTION SYSTEM",
            "experience":[{"company name":"Hexaware Technologies",
                          "posting":"project leader",
                          "duration":1.5},
                          {"company name":"Zoho",
                          "posting":"project manager",
                          "duration":1},
                          {"company name":"UST Global",
                          "posting":"project leader",
                          "duration":1.3}],
            "hobbies":["reading books","playing with dog"],
            "personal details":[{"father's name":"R.Perumal",
                                "father's occupation":"coolie",
                                "languages known":["tamil","english"],
                                "DOB":25-11-2001,
                                "gender":"female",
                                "martial status":"single",
                                "address":{"door no":"4-66A",
                                           "place":"Moolachenvilai",
                                           "post":"Chunkankadi p.o",
                                           "pincode":629801,
                                           "state":"Tamilnadu",
                                           "district":"Kanyakumari"}}]}



for i in my_resume["personal details"]:
    print(i["address"]["place"])

for i in my_resume["educational qualification"]:
    print(i["qualification"])

for i in my_resume["personal details"]:
    print(i["address"]["pincode"])



print(my_resume["educational qualification"][2]["cgpa"])