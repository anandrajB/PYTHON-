#list join
list1=[[4,5,6],[2,3,7],[1,4,8]]
list2=[]
for i in list1:
    list2=i+list2
print(list2)

#list join2
list1=[[4,5,6],[2,3,7],[1,4,8]]
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
    print(list2)
    
#list sort

a=[[1,2],[4,7],[9,12],[3,4]]
b=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
           a[i],a[j]=a[j],a[i]
print(a)
