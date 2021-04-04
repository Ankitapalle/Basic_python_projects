import random

F1 = input("Enter the female name: ")
M1 = input("Enter the male name: ")

Flen = len(F1)
Mlen = len(M1)
x=0
y=0
for i in F1:
    x += ord(i)
for j in M1:
    y += ord(i)

sum1 = x + y
Blen = Flen + Mlen

Blen /= 4
sum1 /= Blen

if sum1<=100:
    print("the Love between you and your partner is " + str(sum1))
else:
    print(random.randint(90,100))



