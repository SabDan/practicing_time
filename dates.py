"""
from datetime import datetime
from datetime import date
from datetime import timedelta

todaydate = date.today()
flag_day = date(2020, 6, 14)
if flag_day is not todaydate:
    print("Sorry there are still " + str((flag_day - todaydate).days) + " until Flag Day.")
else:
    print("It's Flag Day!")
"""
"""
t = timedelta(days=4, hours=10)
t.days()
t.seconds()
t.hours() # invalid

t.seconds /60/60 # 10.0 - seconds divided by 60 sec and 60 min

eta = timedelta(hours=6)
today = datetime.today()
str(today + eta)
# 2020-02-09 20:30:19.197404

datetime.date()

today = datetime.today()

type(today)

"""

# Pomodoro Timer

from datetime import datetime
from datetime import timedelta
import time

seconds = int(input("How many seconds to wait?: "))
for i in range(seconds):
    print(str(seconds - i) + " seconds remain")
    time.sleep(1)




