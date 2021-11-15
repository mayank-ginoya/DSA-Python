import QueueLinkedList as  queue

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
def insertNode(rootNode,newNode):
    if rootNode.data == None:
        rootNode.data = newNode
    elif newNode <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(newNode)
        else:
            insertNode(rootNode.leftChild,newNode)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(newNode)
        else:
            insertNode(rootNode.rightChild,newNode)
    return f"{newNode} is Inserted"

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

def postOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    inOrder(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrder(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode,value):
    if not rootNode:
        return
    if rootNode.data ==  value:
        return "Value Found"
    elif rootNode.data > value:
        if rootNode.leftChild.data == value:
            return "Value Found"
        searchNode(rootNode.leftChild,value)
    else:
        if rootNode.rightChild.data == value:
            return "Value Found"
        searchNode(rootNode.rightChild,value)
    return "Value not found"

def minValueNode(bstNode):
    current =bstNode
    while current.leftChild is not None:
        current=current.leftChild
    return current

def delNode(rootNode,nodeValue):
    if rootNode == None:
        return
    if nodeValue < rootNode.data:
        rootNode.leftChild = delNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = delNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild == None:
            temp,rootNode = rootNode.rightChild,None
            return temp
        if rootNode.rightChild == None:
            temp,rootNode = rootNode.leftChild,None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = delNode(rootNode.rightChild,temp.data)
    return rootNode        

    
newBST = BSTNode(50)
print(insertNode(newBST,20))
print(insertNode(newBST,80))
print(insertNode(newBST,44))
print(insertNode(newBST,40))
print(insertNode(newBST,87))
print(insertNode(newBST,32))
inOrder(newBST)
print("")
levelOrder(newBST)
delNode(newBST,44)  
print("")
inOrder(newBST)    