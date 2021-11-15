#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        print(f'queue = {queue}')
        while queue:
            path = queue.pop(0)
            print(f'Path = {path}')
            print(f'queue = {queue}')
            node = path[-1]
            print(f'node = {node}')
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                print(f'new_path = {new_path}')
                new_path.append(adjacent)
                print(f'new_path = {new_path}')
                queue.append(new_path)
                print(f'queue = {queue}')
                print("\n")

#   queue = [a]
#   path = [a]  queue=[]
#   node = [a]
#   new_path = [a]  
#   new_path = [a,b]
#   queue = [a,b]

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e", "b"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f","a"]
            }

g = Graph(customDict)
ans = g.bfs("c", "a")
print(f'Shortest Part is {ans} and length is {len(ans)}')
