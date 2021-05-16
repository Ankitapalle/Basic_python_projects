"""Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java"""

print(input("Enter file name::\t").split('.')[-1], 'file')