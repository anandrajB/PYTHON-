#TASK 2 (HOMEWORK)
'''
var=input("ENTER A WORD : ")
x,y,z="hot","cold","rainy"
if var==x:
    print("hey !!!! drink water")
elif var==y:
    print("wear a jacket !!! ")
elif var==z:
    print(" get an umbrella")
else:
    print(" SORRY I CAN'T UNDERSTAND ")

#LEAP YEAR 2
'''
year=int(input("ENTER YEAR : "))
if (year%4==0 or year%100==0 or year%400==0):
    print("it is a leap year")
else :
    print("not a leap year")
    
#DEGREE CONVERSION 
var=float(input("ENTER YOUR VALUE :"))
NUM=input(" Enter choice(C/F): ").upper()
F=(var * 9/5) + 32  #farenheit formula
C=(var - 32) * 5/9  #celcius formula
if NUM=='F':
   print("the temperature in celcius is " ,C)
elif NUM=='C':
   print("the temperature in farenheit is " ,F)
    

