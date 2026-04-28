from __future__ import print_function
import schedule
import time
import os
import sys

def hourly():

    print("Task cron: Hourly task executed at", time.strftime("%Y-%m-%d %H:%M:%S"))

schedule.every().hour.do(hourly)

print("Cron scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)


# Old Code
# from __future__ import print_function

# import schedule
# import time
# import os

# def hourly():
#     os.system('powershift image jobs hourly')

# schedule.every().hour.do(hourly)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
