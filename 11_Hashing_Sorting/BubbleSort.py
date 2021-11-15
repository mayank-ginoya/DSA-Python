def bubbleSort(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(l-i-1):
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j]=lst[j],lst[j+1]
    return lst

lst = [2,4,3,9,1,7,8,4]
print(bubbleSort(lst))
