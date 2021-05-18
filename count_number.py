"""Write a Python program to count the number 4 in a given list"""

from typing import Container


n = list(input("Enter the list"))
c=0
print(n)

for i in n:
    if int(i) == 4:
        c+=1
    else:
        continue
print(c)