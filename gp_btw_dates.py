"""Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""


from datetime import date

n = int(input("Enter date"))
a = int(input("Enter month"))
b = int(input("Enter year"))

c = int(input("Enter date"))
d = int(input("Enter month"))
e = int(input("Enter year"))

x = date(b,a,n)
y = date(e,d,c)
z = y - x
print(z.days)


