import random
import time

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%B %d %Y %I:%M %p', prop)
a=random.random()
def return_dates():
    r1=random_date("January 1 2020 1:30 PM", "May 5 2020 4:50 AM",a)
    r2=random_date(r1, "May 5 2020 4:50 AM",a)
    return r1,r2