#bubble sort
a = [99,345,34,54,3,4,6,44,345,4]
j=0
for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print (a) 


#calculator program 
import oldcalculator as OC
def power(a,b):
    return a**b
choice=input("enter your choice (add-sub-mul-div-power): ").lower()
num1=float(input("enter the 1st number : "))
num2=float(input("enter the 2nd number : "))
if choice=="add":
    print(num1,"+",num2,"=" ,OC.add(num1,num2))
elif choice=="sub" :
    print(num1 ,"-" ,num2 ,"=" ,OC.sub(num1,num2))
elif choice=="mul" :
    print(num1 ,"*" ,num2 ,"=" ,OC.multiply(num1,num2))
elif choice=="div":
    print(num1 ,"/" ,num2 ,"=" ,OC.divide(num1,num2))
else:
    print("invalid")


#defining functions for calculator

def add(x, y):
   return x + y
def sub(x, y):q
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y

#pass by value and reference
a=[10,20,30]
def change(b):
    print("before",b,a)
    b[0]=100
    b[1]=200
    print("after",b,a)
change(a)
