monthly_gold_rate=[{"month":"jan",
                    "gold_rate":1000,
                    "jewellery_list":[{"name":"chain","making_cost":12},
                                      {"name":"ring","making_cost":14}]},
                    {"month":"feb",
                    "gold_rate":1500,
                    "jewellery_list":[{"name":"chain","making_cost":12},
                                      {"name":"ring","making_cost":14}]},
                    {"month":"march",
                    "gold_rate":1200,
                    "jewellery_list":[{"name":"chain","making_cost":12},
                                      {"name":"ring","making_cost":14}]},
                    {"month":"april",
                    "gold_rate":900,
                    "jewellery_list":[{"name":"chain","making_cost":12},
                                      {"name":"ring","making_cost":14}]}]

for i in monthly_gold_rate:
    rates=i["gold_rate"]
    months=i["month"]
    for a in i["jewellery_list"]:
        # print(a)
        
        jewellery1=a["making_cost"]
        gold_rate1=rates+(jewellery1/100)
        dict={"month":months,"gold_rate":rates,"jewellery_rate":[{"chain_rate":gold_rate1},{"ring_rate":gold_rate1}]}
        print(dict)