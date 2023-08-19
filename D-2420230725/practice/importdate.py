from datetime import date
# curr_date=date(2023,7,25)
# curr_date=date.today().month
# curr_date=date.today().year
# curr_date=date.today()
curr_date=date.today().day
print(curr_date)

from datetime import time
# curr_time=time(12,15,20)
# curr_time=time(12,15,20).hour
# curr_time=time(12,15,20).minute
curr_time=time(12,15,20).second
# curr_time=time.hours
print(curr_time)

from datetime import datetime
# curr_datetime=datetime(2023,7,25,12,29,20)
# curr_datetime=datetime(2023,7,25,12,29,20).second
# curr_datetime=datetime.today().day
# curr_datetime=datetime.today().year
# curr_datetime=datetime(2023,7,25,12,29,20).hour
curr_datetime=datetime.now()
# curr_datetime=curr_datetime.strftime("%Y")
# curr_datetime=curr_datetime.strftime("%D")
# curr_datetime=curr_datetime.strftime("%S")
# curr_datetime=curr_datetime.strftime("%M")
curr_datetime=curr_datetime.strftime("%m")
# curr_datetime=curr_datetime.strftime("%H")
# curr_datetime=curr_datetime.strftime("%d")
# curr_datetime=curr_datetime.strftime("%y")
# curr_datetime=curr_datetime.strftime("%s")
# curr_datetime=curr_datetime.strftime("%h")
print(curr_datetime)

import pytz
curr_time=pytz.timezone("Asia/Kolkata")
curr_datetime=datetime.now(curr_time)
print(curr_datetime)

from datetime import datetime
d1="26 July, 2023"
# print(type(d1))
curr_date=datetime.strptime(d1,"%d %B, %Y")
print(curr_date)


from datetime import timedelta
# end_date=curr_date+timedelta(days=5)
end_date=curr_date-timedelta(days=5)
print(end_date)


from datetime import datetime
dt_obj = datetime.strptime("2021-08-05 15:25:56.792554",
                           "%Y-%m-%d %H:%M:%S.%f")
nano_secs = dt_obj.strftime("%f")
print(nano_secs)


from dateutil.parser import parse
dt = parse('Mon Feb 15 2010')
print(dt)
# datetime.datetime(2010, 2, 15, 0, 0)
print(dt.strftime('%d/%m/%Y'))



