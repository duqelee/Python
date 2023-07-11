#import time
#print(time.time())

#print(time.localtime())
#tm = time.localtime()
#print(tm.tm_year, "년")
#print(tm.tm_mon, "월")
#print(tm.tm_mday, "일")
#print(tm.tm_hour, "시")
#print(tm.tm_min, "분")
#print(tm.tm_sec, "초")

#now = time.localtime()
#print(time.strftime("%Y%m%d", now))
#print(time.strftime("%c", now))
#print(time.strftime("%x", now))
#print(time.strftime("%X", now))
#print(time.strftime("%H시 %M분 %S초", now))

import datetime
print(datetime.datetime.today())
print(datetime.datetime.today().year)
