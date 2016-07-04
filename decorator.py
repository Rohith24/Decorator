import time
def profile_count(recursion=True):
    profile_count.flag=1
    def wrap(func):
        def inner(n):
            if recursion==True:
                if(n == profile_count.flag+1):
                    profile_count.flag = n
                    inner.count+=1
            else:
                inner.count+=1
            return func(n)
        if recursion==True:
            inner.count=1
        else:
            inner.count=0
        return inner
    return wrap

def profile_time():
    def wrap(func):
        def inner(n):
            start=time.clock()
            retvalue=func(n)
            end=time.clock()
            inner.pro_time += start - end
            return retvalue
        inner.pro_time=0
        return inner
    return wrap

def test_calls_decorator():
    #@profile_count(recursion=False)
    @profile_time()
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n-1) + fib(n-2)

    print [fib(i) for i in range(1,6)]
    print fib.pro_time # all calls counted.


test_calls_decorator()