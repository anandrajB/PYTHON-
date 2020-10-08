#age detection

age=int(input("enter your age: "))
if age<=10:
    print("child")
elif 10<age<=25:
    if age<=18:
        print("school student")
    else :
        print("college student")
elif 25<age<=50:
    if 25<age<=35:
        print("employee")
    elif 35<age<=45:
        print("manager")
    else :
        print("senior manager")
if 50<age<=60:
    print("VRS")
if age>61:
    print("SENIOR CITIZEN")
print()


#Leap year

year=int(input("ENTER YEAR : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else :
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
    
#leap year 2

year=int(input("ENTER YEAR : "))
if year%4==0 and year%100!=0 or year%400==0 :
    print("leap year")
else :
    print("not a leap year")

