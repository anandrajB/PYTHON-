#class with object
'''
x=100
print('hai')
class OldCalc():
    print('hello')
    y=200
    x=300
    print(x+y)
    def add(self,x,y):
        return x+y
    def sub(self,a,b):
        return a-b

class NewCalc():
    x=400
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    
class ModernCalc(OldCalc,NewCalc):
    def power(self,x,y):
        return x**y
    
obj=ModernCalc()
print(obj.x)
'''
#constructor
class NewCalc():
    def __init__(self,x,y):
        print('hello')
        self.x=x
        self.y=y
    def mul(self):
        return self.x*self.y
    def div(self,x,y):
        
        return x/y,self.x/self.y
    
class ModernCalc(NewCalc):
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        super(ModernCalc,self).__init__(c,d)
    def power(self,x,y):
        return x**y,self.a/self.b
obj=ModernCalc(30,20,5,2)
#print(obj.mul())
print(obj.div(9,3))
