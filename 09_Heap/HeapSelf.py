class Heap:
    def __init__(self,size):
        self.customList  = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = 1 + size
    
def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeOfheap(rootNode):
    if not rootNode:
        return 
    return rootNode.heapSize

def levelOrder(rootNode):
    if not rootNode:
        return
    print(*rootNode.customList[1:rootNode.heapSize+1],sep =" -> ")

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex = int(index//2)
    if index <=1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType =="Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertHeap(rootNode,nodeValue,heapType="Min"):
    if rootNode.heapSize+1 == rootNode.maxSize:
        return "Binary Heap is Full"
    rootNode.customList[rootNode.heapSize +1]=nodeValue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return f"{nodeValue} Inserted"

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex = index*2
    rightIndex =  index*2 + 1
    swapchild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if  heapType=="Min":
            if rootNode.customList[index] >  rootNode.customList[leftIndex]:
                rootNode.customList[index],rootNode.customList[leftIndex]=rootNode.customList[leftIndex],rootNode.customList[index]
            return 
        else:
            if rootNode.customList[index] <  rootNode.customList[leftIndex]:
                rootNode.customList[index],rootNode.customList[leftIndex]=rootNode.customList[leftIndex],rootNode.customList[index]
            return 
    else:
        if heapType=="Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapchild]:
                rootNode.customList[index],rootNode.customList[swapchild]=rootNode.customList[swapchild],rootNode.customList[index]     
        elif heapType=="Max":
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapchild]:
                rootNode.customList[index],rootNode.customList[swapchild]=rootNode.customList[swapchild],rootNode.customList[index]
    heapifyTreeExtract(rootNode,swapchild,heapType)

def extractNode(rootNode,heapType="Min"):
    if rootNode.heapSize == 0:
        return
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize] 
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode,1,heapType)
    return extractedNode 


newBinaryHeap=Heap(10)
print(insertHeap(newBinaryHeap,4))
print(insertHeap(newBinaryHeap,9))
print(insertHeap(newBinaryHeap,2))
print(insertHeap(newBinaryHeap,6))
print(insertHeap(newBinaryHeap,3))
print(insertHeap(newBinaryHeap,5))
levelOrder(newBinaryHeap)
extractNode(newBinaryHeap,1)


