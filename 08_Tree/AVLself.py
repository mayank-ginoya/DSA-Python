import QueueLinkedList as queue

class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

def getHeight(rootNode):
    if not rootNode:
        return
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot =disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.righChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.LeftChild,nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    # Left Left Rotation -> (Right Rotation of Node)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    # left Right Rotation -> ( Left Rotation of child + Right Rotation of Node )
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # Right Rotation -> (Left Rotation of Node)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    # Right Left Rotation -> (Right Rotation of child + Left Rotation of Node)
    if balance < -1 and nodeValue < rootNode.leftChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValue(rootNode.leftChild)

def delNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = delNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = delNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp,rootNode=rootNode.rightChild,None
            return temp
        elif rootNode.rightgChild is None:
            temp,rootNode=rootNode.leftChild,None
            return temp
        temp = getMinValue(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild = delNode(rootNode.rightChild,temp.data)
    balance = getBalance(rootNode)
    # LL Condition
    if balance > 1 and getBalance(rootNode.leftChild)>=0:
        return rightRotate(rootNode)
    # RR Condition
    if balance < 1 and getBalance(rootNode.rightChild) <=0:
        return leftRotate(rootNode)
    # lR Condition
    if balance>0 and getBalance(rootNode.leftChild)<0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # RL Condition
    if balance<0 and getBalance(rootNode.rightChild)>0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
    




newAVl = AVLNode(10)
newAVl = insertNode(newAVl,12)
newAVl = insertNode(newAVl,20)
newAVl = insertNode(newAVl,65)
newAVl = insertNode(newAVl,40)
newAVl = insertNode(newAVl,8)
newAVl = insertNode(newAVl,2)
levelOrderTraversal(newAVl)