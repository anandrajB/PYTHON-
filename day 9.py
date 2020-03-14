'''
#prime number
num=int(input("enter a number : "))
for i in range(2,num):
    if (int(num)%i) == 0:
        print("It is not prime number")
        break
else:
    print("It is a prime number")
    

#fibonacci
limit=int(input("enter the limit : "))
x,y=0,1
for i in range(limit):
    print(y)
    x,y = y,x+y
  
#diff between sum of sq and sq of sum
N=int(input("enter a number : "))
x,y=0,0
for i in range(1,N+1):
    x+=i**2
    y+=i
print(abs(x-y**2))
    
#missing number in list
a=[2,4,5,6,8,9]
a.sort()
for i in range(a[0],a[-1]):  
    if i not in a:
        print(i,end=',')
'''
#activity2
started=False
while True:
    var=input("ENTER A WORD : ").lower()
    if var=="start":
            if var=="start":
                if started:
                    print("car already started")
                else:
                    print("start the car")
                    started=True
    elif var=="stop":
            if var=="stop":
                if not started:
                    print("car already stopped")
                else:
                    print("stop the car")
                    started=False
    elif var=="help":
        print('''TO start.......... start the car
TO stop .......... stop the car
TO help .......... more options ''')
    elif var=="exit" and "clear":
        break
    else:
        print(" SORRY I DON'T UNDERSTAND ")
