import datetime
print("------------------------------------------")

print("Date")

print("------------------------------------------")

currd=datetime.datetime.now()
print(currd)


print("------------------------------------------")

#set todays Date
My=datetime.date(2022,1,26)
print(My)

print("------------------------------------------")

#to print sepreate year
print(My.year)

print("------------------------------------------")

#to print sepreate  month
print(My.month)

print("------------------------------------------")

#to print sepreate day
print(My.day)


print("------------------------------------------")

#to give datatime a variable

from datetime import date
mo=date(2022,1,26)
print(mo)

print("------------------------------------------")

#today date
t=date.today()
print(t)

print("------------------------------------------")

print("Time")

print("------------------------------------------")

from datetime import time

a=time()
print(a)

print("------------------------------------------")

t1=time(12,45,54)
print(t1)

print("------------------------------------------")

t2=time(hour=12,minute=54,second=54)
print(t2)

print("------------------------------------------")

#mircrosecond
t3=time(hour=12,minute=54,second=54,microsecond=22223)
print(t3)

print("------------------------------------------")

#onlyminute
print(t3.minute)

print("------------------------------------------")

#onlyhour
print(t3.hour)

print("------------------------------------------")

#onlysecond
print(t3.second)

print("------------------------------------------")

#to manage both

from datetime import datetime
dt=datetime(2022,1,26,12,10,22,36589)
print(dt)

print("------------------------------------------")

#manage date and time
t3=datetime(2022,1,26,12,10,22,36589)
t4=datetime(1999,1,31,18,2,22,35236)
t5=t3-t4
print(t5)

print("------------------------------------------")

currd=datetime.now()
print(currd)

print("------------------------------------------")

#to print datetime in own format
t6=currd.strftime("%H:%M:%S")
print(t6)

print("------------------------------------------")

t7=currd.strftime("%d/%m/%y")
print(t7)
print("------------------------------------------")

#string to date
str="26 january ,2022"
str1=datetime.strptime(str,"%d %B ,%Y")
print(str1)

print("------------------------------------------")

#timezone
from datetime import datetime
import pytz

Us_t=pytz.timezone('America/New_York')
C_t=datetime.now(Us_t)
print(C_t)

print("------------------------------------------")

