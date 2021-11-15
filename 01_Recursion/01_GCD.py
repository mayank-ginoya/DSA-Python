def GCD(a,b):
    assert int(a)==a and int(b)==a,'Numbers Must be Integer'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

n=int(input())
b=int(input())
print(GCD(n,b))