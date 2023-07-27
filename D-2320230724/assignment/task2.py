monthly_gold_rate=[{"month":"jan",
                    "gold_rate":1000},
                    {"month":"feb",
                    "gold_rate":1500},
                    {"month":"march",
                    "gold_rate":1200},
                    {"month":"april",
                    "gold_rate":900},
                    {"month":"may",
                    "gold_rate":1900}]


rate_min=monthly_gold_rate[0]["gold_rate"]
month_min=monthly_gold_rate[0]["month"]
rate_max=0
month_max=monthly_gold_rate[0]["month"]
for i in monthly_gold_rate:
   
    if rate_min>i["gold_rate"]:
        rate_min=i["gold_rate"]
   
        month_min=i["month"]
    elif rate_max<i["gold_rate"]:
        
        rate_max=i["gold_rate"]
    
        month_max=i["month"]
# print(number)
dict={"month1":month_max,
      "gold_rate1":rate_max,
      "month2":month_min,
      "gold_rate2":rate_min}
print(dict)
# print(f"month :{month_min},gold_rate :{rate_min}")
# print(f"month :{month_max},gold_rate :{rate_max}")
    