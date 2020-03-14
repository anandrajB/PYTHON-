#pattern 1
num=int(input("enter the number :"))
for i in range(1,num+1):
    print(i*i)
    
#pattern {floyds triangle}

num=int(input("enter a number :"))
k=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(k,end =" ")
        k=k+1
    print()
    
#pattern 2
num=int(input("enter a number :"))
k=1
for i in range(1,num+1):
    for j in range(1,i+k):
        print(j,end=" ")
    k=k+1
    print()

#pattern 2

num=int(input("enter a number :"))
for i in range(1,num+1,-1):
    for j in range(i):
        print(i,end=" ")
    print()

#pattern 2
num=int(input("enter a number :"))
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#int to string conversion
a=input("enter the number :").split()
for i in range(len(a)):
    a[i]=int(a[i])
    print(a)

    
#length of list
length=int(input("enter the length : "))
b=[]
for i in range(length):
        a=int(input("enter the number : "))
        b.append(a)
print(b)

#unpacking arguments
def add(*arg):
    sum1=0
    for i in a:
        sum1=sum1+i
    return(10,203,4040)

#unpacking argument for dictionary

def dicn(**kwarg):
    for i,j in dict.items(kwarg):
        print(i,j)
dicn(a='apple',b='ball',c='cat')


#pyramid traingle 
#upper
n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
#lower
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()

#paranthesis checking

num=input("enter value : ")
list1 = ["[","{","("] 
list2 = ["]","}",")"]
j=1
for i in range(len(num)//2):
    if num[i] in list1:
        if list2[list1.index(num[i])]!=num[-j]:
            print("invalid")
            break
        else:
            j=j+1
else:
    print("valid")