#pattern printing
n=int(input("enter your range :"))
for i in range(n+1):
    for j in range(i):
        print(i,end="")
    print("\r")
  
#phone keypad using dictionary
key={"1":".@,","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
keypad=input("enter the number : ")
click=int(input("enter the click : "))
if keypad=="7" or "9":
    print(key[keypad][click%4-1])
else:
    print(key[keypad][click%3-1])
  

#count operation using set 
a="hi how are you i am fine "
b=set(list(a))
for i in b:
    print(i,a.count(i))
