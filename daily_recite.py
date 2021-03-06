import csv
import time

def skip_Sunday(e_day, start_weekday):
	e_day = e_day + start_weekday + 1
	e_day -= int(e_day/7)
	e_day = e_day - (start_weekday + 1) 
	return e_day                        
	
fn = 'acts.csv'
with open(fn) as csvFile:
	csvReader = csv.reader(csvFile)
	listReport = list(csvReader)

date_start = "6 Mar 2021 00:00:00"
obj1 = time.strptime(date_start, "%d %b %Y %H:%M:%S")
time_start = int(time.mktime(obj1))

date_now = "8 Mar 2021 08:00:00"
obj2 = time.strptime(date_now, "%d %b %Y %H:%M:%S") 
#time_now = int(time.time())
time_now =int(time.mktime(obj2)) 
e_day = int((time_now - time_start)/86400)
	
#today = time.localtime()
today = obj2
e_day = skip_Sunday(e_day, obj1.tm_wday)

if today.tm_wday == 6:
	print(date_now)
	print("Lord's day, Rest in the Lord!")
	pass

else:
	print("{}/{} 背經Day {}\n".format(today.tm_mon, today.tm_mday, e_day+1))
	if (e_day == 0):
		for i in range(2):	
			row = listReport[i]
			message = "徒{}:{} {}\n".format(row[0], row[1], row[2])

	else:
		for i in range(2*e_day-2, 2*e_day+2):
			row = listReport[i]
			message = "徒{}:{} {}\n".format(row[0], row[1], row[2])

token = '6R7E6JodLB5RAaH2N7DuZjlLnXqZHglmSBZGElrWwY2'
result = lineNotifyMessage(token, message)
print(result) # 印一下回傳代碼
