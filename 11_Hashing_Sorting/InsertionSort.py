def insertionSort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and key<lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst

lst = [2,4,3,9,1,7,8,4]
print(insertionSort(lst))
