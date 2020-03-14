'''def fun1(fun2):
    def innerfun():
        print(fun2)
        print("i got decorator")
        fun2()
    return innerfun

@fun1
def ordinary():
    print("I am ordinary")

#ordinary()



def fun1(fun2):
    
    print("i got decorator")
    fun2()
    return fun1

@fun1
def ordinary():
    print("I am ordinary")



'''

def isloggedin(func):
    def check():
        login =True
        print("checking")
        if login == True:
            print(func)
            func()
        else:
            print("login failed")
    print('hai')
    return check

#@isloggedin
def ordinary():
    print ("i am ordinary")

@isloggedin
def show_profile():
    print("Myprofile")

ordinary()
show_profile()
