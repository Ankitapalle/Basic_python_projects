"""Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""

date = int(input("Enter the date - "))
month = int(input("Enter the month - "))
year = int(input("Enter the year - "))
exam_st_date = (date,month,year)
print("The date of exam is %i/%i/%i"%exam_st_date)
