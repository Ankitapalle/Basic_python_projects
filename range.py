"""Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum."""

from typing import cast


a = int(input('Enter first number::'))
b = int(input('Enter Second number::'))
c = int(input('Enter Third number::'))

s = a+b+c
if a == b == c:
    ts=s+s+s
    print(ts)
else:
    print(s)