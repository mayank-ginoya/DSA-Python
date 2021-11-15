def findMinOperation(s1, s2,index1=0,index2=0,memo={}):
    # TODO
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1,s2,index1+1,index2+1,memo)
    else:
        dictKey = str(index1)+str(index2)
        if dictKey not in memo:
            delOp = 1 + findMinOperation(s1,s2,index1+1,index2,memo)
            updateOp = 1 + findMinOperation(s1,s2,index1+1,index2+1,memo)
            insertOp = 1 + findMinOperation(s1,s2,index1,index2+1,memo)
            memo[dictKey] = min(delOp,insertOp,updateOp)
        return memo[dictKey]

print(findMinOperation("table", "tbrltt", 0, 0,{}))

