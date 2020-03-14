'''def factorial(n):
    #print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        #print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(5))

'''

def fib(n):
    print("factorial has been called with n = " + str(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res=fib(n-1) + fib(n-2)
        print("intermediate result for ", n, "  fib: ",res)
        return res


print(fib(5))

