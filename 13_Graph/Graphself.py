class Graph:
    def __init__(self,gdict=None) -> None:
        if gdict == None:
            self.gdict ={}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for av in self.gdict[deVertex]:
                if av not in visited:
                    visited.append(av)
                    queue.append(av)

    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for av in self.gdict[popVertex]:
                if av not in visited:
                    visited.append(av)
                    stack.append(av)


customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f"],
            "f" : ["d", "e"]
            }
graph = Graph(customDict)
graph.addEdge("e","c")
#print(str(graph.gdict).replace('],' , ']\n'))
graph.bfs("a")
print()
graph.dfs("a")