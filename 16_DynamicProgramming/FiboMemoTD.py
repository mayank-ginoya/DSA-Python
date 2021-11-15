def FibMemo(n,memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = FibMemo(n-1,memo) + FibMemo(n-2,memo)
    #print(memo.values())
    return memo[n]

myDict = {}
print(FibMemo(5,myDict))
print(list(myDict.values()))