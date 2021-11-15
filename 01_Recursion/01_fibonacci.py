def fib(n):
    assert n>=0 and int(n)==n,'Number Must be Positive and Integer'
    if n in [0,1]:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input())
print(fib(n))
