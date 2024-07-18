# module daytime
# from datetime import datetime # cause error cause datetime.datetime not ok
import datetime
# date, time, datetime, timedelta

dnt = datetime.datetime(2024, 7, 17, 14, 13, 00)
dat = datetime.date(2024, 7, 18)

print(dnt)
# 2024-07-17 14:13:00

print(dat)
# 2024-07-18

print(dir(datetime))
'''
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'date', 'datetime', 
'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''

from datetime import datetime
n = datetime.now()
print(n.strftime('%A-%d-%m-%Y'))

d = "2/9/2024"
da = datetime.strptime(d, "%d/%m/%Y")
print(da)

import pytz

tz = pytz.timezone("Asia/Ho_Chi_Minh")
d = datetime.now(tz)
print(d)

tz = pytz.timezone("Asia/Hong_Kong")
d = datetime.now(tz)
print(d)