#sort
a= [2,6,3,8,9,4,5]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
           a[i],a[j]=a[j],a[i]
print("The sorted list is ",a)

#max
a= [2,6,3,8,9,4,5]
count=a[0]
for i in a:
    if i>count:
        count=i
print("the max number is ",count)

#min
a= [2,6,3,8,9,4,5]
count=a[0]
for i in a:
    if i<count:
        count=i
print("the min number is ",count)

#duplication delete
a=[4,4,2,2,4,3,3,1]
b=[]
for i in a:
    if i not in b:
        b.append(i)
a=b.copy()
print("the list is ",a)