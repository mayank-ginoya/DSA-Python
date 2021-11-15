class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self,word):
        current = self.root
        word = word.upper()
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString =  True
        return f"{word:5} is SuccessFull Inserted"
    
    def searchString(self,word):
        current = self.root
        word = word.upper()
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        return False
    
def delString(root,word,index):
    ch = word[index]
    current = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(current.children)>1:
        delString(current,word,index+1)
        return False
    
    if index == len(word)-1:
        if len(current.children)>=1:
            current.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if current.endOfString == True:
        delString(current,word,index+1)
        return False
    
    canThisNodeBeDeleted = delString(current,word,index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
    else:
        return False







newTrie = Trie()
print(newTrie.insertString("APP"))
print(newTrie.insertString("API"))
print(newTrie.insertString("APIS"))
print(newTrie.insertString("APS"))
print(newTrie.searchString("appl"))
print(newTrie.searchString("app"))
print(delString(newTrie,"app",0))