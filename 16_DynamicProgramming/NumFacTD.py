def numFactTD(n,memo):
    if n in range(0,3):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numFactTD(n-1,memo)
        subP2 = numFactTD(n-3,memo)
        subP3 = numFactTD(n-4,memo)
        memo[n] = subP1 + subP2 + subP3
        return memo[n]
myDict = {}
print(numFactTD(5,myDict))
