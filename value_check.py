"""Write a Python program to check whether a specified value is contained in a group of values"""
n = int(input("Enter value"))

txt = [3,5,4,5,74]
for i in txt:
    if txt == n:
        print("value is in the group")
        break
    else:
        print("Value is not in the group")
        

