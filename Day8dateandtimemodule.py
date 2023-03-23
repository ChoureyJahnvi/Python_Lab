import datetime
from datetime import date
# to print the date(yyyy-mm-dd) and time
AtPresent= datetime.datetime.now()
print(AtPresent)

# To print the current date(yyyy-mm-dd)
currentdate = datetime.date.today()
print(currentdate)

# To add days to present date and tell the date:
today = datetime.date.today()
day = int(input("Enter the number of days to add: "))
days = datetime.timedelta(days = day)
added_days = today + days
print(added_days)