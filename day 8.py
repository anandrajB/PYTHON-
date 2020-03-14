    #anagram 
a=list(input("enter a string 1: "))
b=list(input("enter a string 2: "))
a.sort()
b.sort()
print(a,b)
for i in range(len(b)):
    if a[i]!=b[i]:
        print(" not anagram")
        break
else:
    print(" anagram")

    #armstrong
a=input("enter a number :")
sum=0
for i in range(len(a)):
    sum +=int(a[i])**len(a)
if int(a)==sum:
    print(a,"it is armstrong")
else:
    print(a,"not a armstrong")

    # armstrong 2
a= int(input("enter : "))
b=a
sum=0
while b>=1:
    sum+=(b%10)** len(str(a))
    b=b//10
    print(sum)

 #factorial

a=int(input("enter a number :"))
sum=1
for i in range(1,a+1):s
	sum=sum*i
print(sum)