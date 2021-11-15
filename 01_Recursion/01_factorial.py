def fact(n):
    assert n>=0 and int(n)==n,'Number Must be Positive and Integer'
    if n in [0,1]:
        return 1
    else:
        return n*fact((n-1))

n=int(input())
print(fact(n))
