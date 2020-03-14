#method overriding 

class old:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self
    def sub(self,a,b):
        return a-b,self.a-self.b
class new(old):
    def __init__(self,a,b,x,y):
        self.x=x
        self.y=y
        super(new,self).__init__(a,b)
    def mul(self):
        return self
    def sub(self,a,b):
        x=super(new,self).sub(a,b)
        return b-a,self.b-self.a,x
obj=new(10,20,30,40)
print(obj.sub(500,300))

#number square and add
a=(input("enter the number :")).split()
count=0
c=0
for i in range(len(a)):
    a[i]=int(a[i])
for i in a:
    if len(a)== a.count(i): 
        c+=i*i
        print(c)
    else:
        total=sum(a)
        print(total)
    