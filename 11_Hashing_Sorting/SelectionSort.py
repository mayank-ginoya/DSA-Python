def selectionSort(lst):
    l = len(lst)
    for i in range(l):
        min_index = i
        for j in range(i+1,l):
            if lst[i] > lst[j]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst

lst = [2,4,3,9,1,7,8,4]
print(selectionSort(lst))
