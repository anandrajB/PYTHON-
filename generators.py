def fib(mymax):
    a, b = 0, 1
    while True:
        c=a+b
        if c<mymax:
            
            print('before')
            yield c
            print('after')
            a, b = b, c
            print(c)
        else:
            break
     

generator=fib(10)
print(next(generator))
print(next(generator))


'''

for i in range(20):
    
    print('before')
    yield i
    print('after')
    print(i)
'''


