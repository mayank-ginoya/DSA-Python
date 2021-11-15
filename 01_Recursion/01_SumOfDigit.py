def SumOfDigit(n):
    assert n>=0 and int(n)==n,'Number Must be Positive Only'
    if n==0:
        return 0
    else:
        return int(n%10) + SumOfDigit(int(n/10))

n=int(input())
print(SumOfDigit(n))