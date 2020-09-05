import datetime
import calendar

def has_friday_13(month, year):
	x = datetime.datetime(year,month,13)
	return True if calendar.day_name[x.weekday()] == 'Friday' else False
print(has_friday_13(3, 2020))