def numFactTD(n):
    tb = [1,1,1,2]
    for i in range(4,n+1):
        tb.append((tb[n-1] + tb[n-3] + tb[n-4]))
    return tb[n]

print(numFactTD(3))
