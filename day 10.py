#prime number range set

num=int(input("enter your name :"))
for num in range(2,num):
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        print(num)
     

#email and username splitter
        
var=input(" enter a e-mail address : ")
seperate=var.split("@")[0]
seperate1=var.split("@")[1]
print("The username is :",seperate)
print("The hostname is :",seperate1)

#email validator 1

email=input("enter a email address  : ")
var="@"
if var in email:
    print("valid")
else:
    print("invalid email id ")

#prime number position finding
 
var=int(input("enter the position :"))
count=0
for i in range(2,var):
    for j in range(2,i):
        if i%j==0:
            break 
    else:
        count=count+1
        if count==10:
            print("the number is ",i)
            break

#finding 2nd largest number       
a=[2,3,6,6,2,11,4,10,68,4,9]
count=a[0]
count2=0
for i in a:
    if i>count:
        count2=count
        count=i
    elif count>count2<i:
        count2=i
print("the 2nd max number is ",count2)