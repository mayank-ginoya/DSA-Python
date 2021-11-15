def heapify(lst,n,i):
    smallest =  i
    l = i*2 + 1
    r = i*2 + 2
    if l<n and lst[l] < lst[smallest]:
        smallest = l
    if r < n and lst[r] < lst[smallest]:
        smallest = r
    if smallest != i:
        lst[i],lst[smallest] = lst[smallest],lst[i]
        heapify(lst,n,smallest)

def heapSort(lst):
    n=len(lst)
    for i in range(int(n/2)-1,-1,-1):
        heapify(lst,n,i)
    
    for i in range(n-1,0,-1):
        lst[i],lst[0] =  lst[0],lst[i]
        heapify(lst,i,0)
    lst.reverse()

lst = [2,3,6,1,7,0,9,4]
heapSort(lst)
print(lst)