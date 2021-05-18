"""think any of the number but answer should be only 3."""

n = int(input("Enter the number you thought::"))
print("Double the number")
s = n+n
a = input()
print("add 6 in it")
s+=6
b = input()
print("half the number")
s/=2
c = input()
print("remove the number you choose from it")
s-=n
d = input()
print("Your answer is - " + str(s) + ":)")
