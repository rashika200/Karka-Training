# from datetime import date,timedelta
# curr_date=date.today()
# # from datetime import timedelta
# days=int(input("enter the day:"))
# end_time=curr_date+timedelta(days)
# print(end_time)


from datetime import datetime,timedelta
d1=input("enter the date :")
curr_date=datetime.strptime(d1,"%Y %m, %d")
# print(type(curr_date))
days=int(input("enter the day:"))
end_time=curr_date+timedelta(days)
print(end_time)


# from datetime import datetime,timedelta
# d1=input("enter the date :")
# curr_date=d1.strftime("%Y %m, %d")
# days=int(input("enter the day:"))
# end_time=curr_date+timedelta(days)
# print(end_time)


