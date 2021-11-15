from collections import defaultdict

class Graph :
    def __init__(self) -> None:
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def addNode(self,vertex):
        self.nodes.add(vertex)

    def addEdge(self,fromNode,toNode,dist):
        self.edges[fromNode].append(toNode)
        self.distance[fromNode,toNode]=dist

def dijkstra(graph,initial='A'):
    visited = {initial:0}
    path = defaultdict(list)
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in visited:
            if minNode is None:
                minNode = node
            elif visited[node] < visited[minNode]:
                minNode = node
        if minNode is None:
            break
            
        nodes.remove(minNode)
        curWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = curWeight + graph.distance[(minNode,edge)]
            if  edge not in visited or weight < visited:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited,path


g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")
g.addEdge("A", "B", 2)
g.addEdge("A", "C", 5)
g.addEdge("B", "E", 3)
g.addEdge("B", "D", 1)
g.addEdge("B", "C", 6)
g.addEdge("D", "E", 4)
g.addEdge("C", "F", 6)
g.addEdge("E", "G", 9)
g.addEdge("F", "G", 7)
print(g.edges)
print(dijkstra(g))
