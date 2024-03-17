import datetime

# get the current date and time
now = datetime.datetime.now()

print(now)

print(datetime.date.today())

import datetime
print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.time(now).hour)
print(datetime.datetime.time(now).minute)
print(datetime.datetime.time(now).second)

print(datetime.datetime.month.__sizeof__())
# print(datetime.datetime.timestamp())
print(datetime.datetime.utcnow())
# print(datetime.datetime.timetuple())
# print(datetime.datetime.weekday(3))
