import copy


# Your node should implement the following operations:
#   an init method
#   an operation to add a left subtree to a node.
#   an operation to add a right subtree to a node.
#   an operation that computes the height of a node. It can be recursive or non-recursive, but I recommend you implement a recursive version, so that you have some practice with that programming technique.
#   Many, if not all of the operations you have to present for a node have been either included in code available on blackboard, or on pseudo-code seen in class. You can choose to use those, or some of your own creation.

class Node:
    def __init__(self):
        self.__data = None
        self.__edgeList = []

    def SetData(self, n):
        self.__data = n
        return

    def GetData(self):
        return self.__data

    def addEdge(self, n):
        self.__edgeList.append(n)
        return

    def getEdges(self):
        return self.__edgeList

    def deleteEdge(self, n):
        if n in self.getEdges():
            self.__edgeList.remove(n)
        return

    def BFS(self, n, list, queue):
        return

    def __str__(self):
        # stringToPrint = "Data in node      : " + str(self.__data) + "\nParent            : " + str(self.__parent) + "\nnumber of children: " + str(len(self.__listOfChildren)) + "\nChildren          : " + str(self.__listOfChildren)
        stringToPrint = "Data in node      : " + (self.__data) + "\nEdges: " + str(self.getEdges())
        return (stringToPrint)


if (__name__ == "__main__"):
    print("in the main program")
    sampleNode = Node()
    print(sampleNode)
    secondNode = Node()
    secondNode.SetData(1)
    thirdNode = Node()
    thirdNode.SetData(3)
    thirdNode.SetData(4)
    print(sampleNode)
    print(secondNode)
    print(secondNode)
    secondNode.SetData(2)
    print("\nDFT")
    sampleNode.DepthFirstTraversal()
