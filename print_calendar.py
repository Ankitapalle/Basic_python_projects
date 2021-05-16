"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
x = c.formatmonth(2021,5)
print(x)