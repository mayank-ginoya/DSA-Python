import math
from BubbleSort import bubbleSort

def bucketSort(lst):
    noOfBucket = round(math.sqrt(len(lst)))
    maxValue = max(lst)
    arr = []
    for i in range(noOfBucket):
        arr.append([])
    for j in lst:
        index_b = math.ceil(j*noOfBucket/maxValue)
        arr[index_b-1].append(j)
    for i in range(noOfBucket):
        arr[i] = bubbleSort(arr[i])
    k = 0
    for i in range(noOfBucket):
        for j in range(len(arr[i])):
            lst[k] = arr[i][j]
            k += 1
    return lst

lst = [2,4,3,9,1,7,8,4]
bucketSort(lst)