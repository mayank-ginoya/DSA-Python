class BiniaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "BT is Full"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex += 1
        return f"{value} Added"

    def searchNode(self,nodeValue):
        if self.lastUsedIndex==0:
            return "BT is Empty"
        for i in self.customList:
            if i == nodeValue:
                return f"{i} was Found"
        else:
            return f"{nodeValue} not Found"

    def preOrder(self,index):
        if int(index) > int(self.lastUsedIndex):
            return
        print(self.customList[index])
        self.preOrder(index*2)
        self.preOrder(index*2+1)
    
    def inOrder(self,index):
        if int(index) > int(self.lastUsedIndex):
            return
        self.preOrder(index*2)
        print(self.customList[index])
        self.preOrder(index*2+1)
    
    def postOrder(self,index):
        if int(index) > int(self.lastUsedIndex):
            return
        self.preOrder(index*2)
        self.preOrder(index*2+1)
        print(self.customList[index])
        
    def levelOrder(self,index):
        if int(index) > int(self.lastUsedIndex):
            return
        for i in range(index,self.lastUsedIndex):
            print(self.customList[i])

    def delNode(self,value):
        if self.lastUsedIndex==0:
            return None
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex -=1
                return "Node Successfully Deleted"
        return "Node not Found"
    
    def delTree(self):
        self.customList=None
        

newBT =BiniaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Milk"))
print(newBT.insertNode("IceCream"))
print(newBT.searchNode("Milk"))
newBT.preOrder(1)
print()
newBT.inOrder(1)
print()
newBT.postOrder(1)
print()
newBT.levelOrder(1)
print(newBT.delNode("Tea"))
newBT.levelOrder(1)
