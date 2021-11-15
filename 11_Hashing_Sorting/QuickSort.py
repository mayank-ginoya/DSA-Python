def partition(lst,l,h):
    i = l-1
    pivot = lst[h]
    for j in range(l,h):
        if lst[j] <= pivot:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]
    lst[i+1] , lst[h] = lst[h],lst[i+1]
    return (i+1)

def quickSort(lst,l,h):
    if l < h:
        pi = partition(lst,l,h)
        quickSort(lst,l,pi-1)
        quickSort(lst,pi+1,h)
    return lst

lst = [2,3,6,1,7,0,9,4]
print(quickSort(lst,0,len(lst)-1))