# Tien Li Shen
# 8/5/2019
# ECE 241

# This homework will allow you to demonstrate understanding and engagement with the following topics:

#   graphs
#   object oriented programming
#   recursion
#   dictionaries/hash tables
# Your task is to implement a Graph class. The edges in the graph are undirected. Of the four types of graph implementations we saw in class, you should use adjacency lists. The graph should have the following methods:

#   init
#   insertNode(d) : takes data contained as its argument, and adds it into the graph, aterputting the data element into a node
#   deleteNode(d): finds a node with data d in its node, and deletes it. Also deletes all edges from and into it. Prints an error message if no such node exists.
#   insertEdge(a, b): Inserts a new edge between node with data a and node with data b. Prints an error message if either of those nodes does not exist.
#   deleteEdge(a,b): Deletes the edge between a node with data a and a node with data b. Prints an error message if no such edge exists.
#   DFS(d): traverses the graph, starting at the node with data d, using depth first search. prints an error message if no such node exists.
#   BFS(d): traverses the graph, starting at the node with data d, using breath first search. prints an error message if no such node exists
#   FindPath(a,b): Prints the shortest path from node with data a to node with data b. Prints an error message if the path does not exist
#   You should include a main program that tests the features listed above.

# Please pay attention to the scoring rubric provided.

from Node_Graph import Node
from queue_stack_strings_graph import Queue


class Graph:
    def __init__(self):
        self.verticesList = []

    def insertNode(self, d):
        self.verticesList.append(d)
        return

    def deleteNode(self, d):  # all edges to this node has to be deleted
        self.verticesList.remove(d)
        for vertex in self.verticesList:
            vertex.deleteEdge(d)
        return

    def addEdge(self, a, b):
        a.addEdge(b)
        b.addEdge(a)
        return

    def deleteEdge(self, a, b):
        a.deleteEdge(b)
        b.deleteEdge(a)
        return

    def DFS(self, d, list=[]):  # I used the pseudo code provided in the notes to help me implement this method
        list.append(d)
        print(d)
        for edge in d.getEdges():
            if edge not in list:
                return self.DFS(edge, list)

    def BFS(self, d):
        # I used the pseudo code provided in the notes to help me implement this method. Since the method requires quque, I recycled code from week 2 to implement this method
        list = []  # I thought BFS was harder to implement than dfs since it required a queue  and managing breadth
        queue = Queue()
        list.append(d)
        queue.Enqueue(d)
        current = d
        while queue.GetSize() != 0:
            for edge in current.getEdges():
                if edge not in list:
                    list.append(edge)
                    queue.Enqueue(edge)
            current = queue.Dequeue()
            print(current)
        return None



if (__name__ == "__main__"):
    print("in the main program")
    nodeA = Node()
    nodeB = Node()
    nodeC = Node()
    nodeD = Node()
    nodeE = Node()
    nodeA.SetData("A")
    nodeB.SetData("B")
    nodeC.SetData("C")
    nodeD.SetData("D")
    nodeE.SetData("E")
    # Jaime added the line below to test what happens if we try to delete a
    # node that does not exist in the graph
    nodeF = Node()
    nodeF.SetData("F")
    sampleGraph = Graph()
    sampleGraph.insertNode(nodeA)
    sampleGraph.insertNode(nodeB)
    sampleGraph.insertNode(nodeC)
    sampleGraph.insertNode(nodeD)
    sampleGraph.insertNode(nodeE)
    sampleGraph.addEdge(nodeA, nodeB)
    sampleGraph.addEdge(nodeB, nodeC)
    sampleGraph.addEdge(nodeC, nodeD)
    sampleGraph.addEdge(nodeD, nodeE)
    sampleGraph.addEdge(nodeE, nodeA)
    sampleGraph.addEdge(nodeA, nodeC)
    sampleGraph.deleteNode(nodeB)
    # sampleGraph.DFS(nodeC)
    sampleGraph.BFS(nodeA)
    sampleGraph.deleteNode(nodeF)
