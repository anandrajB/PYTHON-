class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):
        self.__name=name
    def getname(self):
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name
    name=property(getname, setname, delname)
'''
p1=person()
p1.setname('bita')
print(p1.getname())'''
#prop=property(getter, setter, deleter, docstring)
    
p1=person()
p1.name='bita'
print(p1.name)
