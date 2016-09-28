# can make something more specialized and just increment months not days

class Calendar:
	days_in_week = 7;

	month_to_days = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }
	feb = 2 #months with extra rules

	def __init__(self, dayOfWeek, firstDay, month, year):
		self.day_of_week = dayOfWeek
		self.current_day = firstDay
		self.current_month = month
		self.current_year = year

	def increment_day(self): 
		#increment day of week
		self.day_of_week = (self.day_of_week + 1)% Calendar.days_in_week
		#increment day of month
		self.current_day = (self.current_day + 1)% self.get_days_in_current_month()
		#if the day started the next month increment month
		if(self.current_day == 0):
			self.current_month += 1
			if(self.current_month not in Calendar.month_to_days):
				self.current_month = min(Calendar.month_to_days)
				self.current_year += 1

	def get_days_in_current_month(self):
		if self.current_month != Calendar.feb:
			return Calendar.month_to_days[self.current_month]
		if self.current_year % 400 == 0:
			return Calendar.month_to_days[self.current_month] + 1
		if self.current_year % 4 == 0 and self.current_year % 100 != 0:
			return Calendar.month_to_days[self.current_month] + 1
		return Calendar.month_to_days[self.current_month]


answer = 0
cal = Calendar(1, 0, 1, 1900)
while(cal.current_year < 2001):
	if(cal.current_day == 0 and cal.day_of_week == 0 and cal.current_year > 1900):
		answer += 1
	cal.increment_day()



