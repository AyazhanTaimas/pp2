from datetime import date, timedelta
yday = date.today() - timedelta(1)
tday = date.today() + timedelta(1)
print("Yesterday: ", yday)
print('Today:', date.today())
print('Tomorrow:', tday)