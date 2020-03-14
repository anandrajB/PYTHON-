# palindrome
'''
x=input("ENTER A STRING : ")
if x==x[::-1]:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
'''

#TASK 1

a="abcd"
b=int(input("enter your value : "))
print ( a[b:] + a[:b] )
