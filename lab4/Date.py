#1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime

current_datetime = datetime.now()
print("With microseconds:", current_datetime)

no_microseconds = current_datetime.replace(microsecond=0)
print("Without microseconds:", no_microseconds)

#4
from datetime import datetime

date1 = datetime(2025, 2, 21, 10, 0, 0)  
date2 = datetime(2025, 2, 21, 12, 30, 0) 

difference = date2 - date1

seconds_difference = difference.total_seconds()

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", seconds_difference)
