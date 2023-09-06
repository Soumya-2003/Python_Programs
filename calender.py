# Program to print a calender of a specified month and year
import calendar
year = int(input("Enter Year: "))
month = int(input("Enter month: "))
print("\n",calendar.month(year,month))