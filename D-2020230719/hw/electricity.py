consumer_data={"consumer name":"P.Rashika",
               "meter_reading":[150,500,1200,1350,2500,3123,4325,6574,8765,8897,9765]}


# name=input("consumer name :")
# reading1=int(input("enter reading1 :"))
# reading2=int(input("enter reading2 :"))
# reading3=int(input("enter reading3 :"))
# reading4=int(input("enter reading4 :"))
# reading5=int(input("enter reading5 :"))
# readings=reading1,reading2,reading3,reading4,reading5
# consumer_data={"consumer name":name,
#                "meter_readings":readings}


# readings=[150,500,1200,1350,2500,3123,4325,6574,8765,8897,9765]
def calculate_electricity_bill(consumer_data):
    readings=consumer_data["meter_reading"]
    list=[]
    for i in range(len(readings)-1): 
        bill_amount=0 
        month=0 
        units=readings[i+1]-readings[i]
        # print(units)
        month=i+1
        if units<100:
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{bill_amount}")
        if units>100 and units<200:
            value=units*2
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{value}")
        if units>200 and units<500:
            value=units*5
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{value}")

        if units>500 and units<1000:
            value=units*10
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{value}")
        if units>1000:
            value=units*14
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{value}")
       
        dict={"month":month,"unit_consumed":units,"bill_amount":bill_amount}
        # print(dict)
        list.append(dict)
            # print(list)
    total=0
    total=total+bill_amount
    print("total amount :",total)
# calculate_electricity_bill(consumer_data)

    text=""
    import json
    name=str(list)
    method=input("enter the method :")
    if method=="json"and"Json"and"JSON"and"JsOn"and"JSon":
        list_json=json.dumps(name)
        print(list_json)
    elif method=="dict":
        list_dict=str(list)
        print(list_dict)


    for data in list:
        text=text+(f"month:{data['month']},\nunit_consumed:{data['unit_consumed']},\nbill_amount:{data['bill_amount']}\n")
        file_name="/home/rashika/rashi.txt"
        with open(file_name,"w")as file:
            # file.write(list_json)
            file.write(list_dict)
            file.close()
calculate_electricity_bill(consumer_data)
