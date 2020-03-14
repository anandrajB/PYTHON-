#class without self/object
'''
x=100
class OldCalc():
    y=200   
    def add(a,b):
        return a+b,a,b
        
    def sub(a,b):
        return a-b

print(OldCalc.add(10,20))
print(OldCalc.y)
'''
#class with object
'''
x=100
class OldCalc():
    y=200   
    def add(self,a,b):
        return a+b,a,b
        
    def sub(self,a,b):
        return a-b
obj=OldCalc()
print(obj.add(10,20))
'''
#class with constructor
'''
x=100
class OldCalc():
    print('hello')
    y=200
    print('hai')
    def __init__(self,a,b):
        print('hello')
        self.a=a
        self.b=b
              
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
        
    def sub(self):
        return self.a-self.b
    a=10
    b=20
    print(a+b)

obj=OldCalc(10,20)
print(obj.add(10,5))
print(obj.sub())
'''
#counting the class

class OldCalc():
    count=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
        OldCalc.count=OldCalc.count+1
        self.count=OldCalc.count
              
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
        
    def sub(self):
        return self.a-self.b




o1=OldCalc(10,20)
o2=OldCalc(10,20)
o3=OldCalc(10,20)
o4=OldCalc(10,20)
print(o2.count)

#inheritance with super
'''
class OldCalc():
    count=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
            
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
        
    def sub(self):
        return self.a-self.b

        
class NewCalc(OldCalc):
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        super(NewCalc,self).__init__(a,b)
    
    def mul(self):
        return self.a*self.b
    
    def sub(self):
        x=super(NewCalc,self).sub()
        return self.b-self.a,x

obj=NewCalc(10,20,10,20)
print(obj.mul())
print(obj.sub())

'''

a=[i for i in range(100) if i%3==0 or i%5==0]
print(a)










