def Power(n,x):
    assert x>=0 and int(x)==x,'Power Should be Positive'
    if x==0:
        return 1
    else:
        return n*Power(n,x-1)

n=float(input())
x=int(input())
print(Power(n, x))