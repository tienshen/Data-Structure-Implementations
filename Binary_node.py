import copy


# Your node should implement the following operations:
#   an init method
#   an operation to add a left subtree to a node.
#   an operation to add a right subtree to a node.
#   an operation that computes the height of a node. It can be recursive or non-recursive, but I recommend you implement a recursive version, so that you have some practice with that programming technique.
#   Many, if not all of the operations you have to present for a node have been either included in code available on blackboard, or on pseudo-code seen in class. You can choose to use those, or some of your own creation.

class Node:
    def __init__(self):
        self.__parent = None
        self.__data = 0
        self.__leftSubtree = None
        self.__rightSubtree = None

    def SetParent(self, e):
        self.__parent = e
        return (self.__parent)

    def SetLeftSubTree(self, n):
        self.AddChildToTheLeft(n)

    def SetRightSubTree(self, n):
        self.AddChildToTheRight(n)

    def GetLeftSubTree(self):
        return (self.__leftSubtree)

    def GetRightSubTree(self):
        return (self.__rightSubtree)

    def GetParent(self):
        return (self.__parent)

    def IAmALeaf(self):
        if (self.GetLeftSubTree() == None and self.GetRightSubTree() == None):
            return (True)
        else:
            return (False)

    def NonRecursiveDepth(self):
        currentNode = self
        currentDepth = 0
        while currentNode != None:
            currentDepth = currentDepth + 1
            currentNode = currentNode.GetParent()

    def GetDepth(self):
        if (self.GetParent() == None):
            # print("i seem to have no parent")
            # I am the root
            return (0)
        else:
            return (1 + self.GetParent().GetDepth())

    def GetHeight(self):
        if (self.IAmALeaf()):
            return (0)
        else:
            if (self.GetLeftSubTree() == None):
                sizeToTheLeft = 0
            else:
                sizeToTheLeft = self.GetLeftSubTree().GetHeight()
            if (self.GetRightSubTree() == None):
                sizeToTheRight = 0
            else:
                sizeToTheRight = self.GetRightSubTree().GetHeight()
            biggestOfEither = max(sizeToTheLeft, sizeToTheRight)
            return (biggestOfEither + 1)

    def AddChildToTheLeft(self, n):
        nodeToAdd = Node()
        nodeToAdd = copy.deepcopy(n)
        self.__leftSubtree = nodeToAdd
        if nodeToAdd != None:
            nodeToAdd.SetParent(self)
        return (self.__leftSubtree)

    def AddChildToTheRight(self, n):
        nodeToAdd = Node()
        nodeToAdd = copy.deepcopy(n)
        self.__rightSubtree = nodeToAdd
        if nodeToAdd != None:
            nodeToAdd.SetParent(self)
        return (self.__rightSubtree)

    def GetChildren(self):
        return ([self.GetLeftSubTree(), self.GetRightSubTree()])

    def GetData(self):
        return (self.__data)

    def SetData(self, d):
        self.__data = d
        return (self.__data)

    def __str__(self):
        children = self.GetChildren()
        if children[0] is not None:
            children[0] = children[0].GetData()
        if children[1] is not None:
            children[1] = children[1].GetData()
        # stringToPrint = "Data in node      : " + str(self.__data) + "\nParent            : " + str(self.__parent) + "\nnumber of children: " + str(len(self.__listOfChildren)) + "\nChildren          : " + str(self.__listOfChildren)
        stringToPrint = "Data in node      : " + str(self.__data) + "\nDepth: " + str(
            self.GetDepth()) + " Height: " + str(self.GetHeight()) + "\nChildren : " + str(children)
        return (stringToPrint)

    def DepthFirstTraversal(
            self):  # traversal definitely had me confused at first since I did not realize that the same method was implemented in both classes
        # first print the root
        print(self)
        # print(self.GetData())
        # print(self.GetChildren())
        # now traverse the children
        if (self.GetLeftSubTree() != None):
            self.GetLeftSubTree().DepthFirstTraversal()
        if (self.GetRightSubTree() != None):
            self.GetRightSubTree().DepthFirstTraversal()
        return (True)

    def InOrderTraversal(self):
        if self.GetLeftSubTree() != None:
            self.GetLeftSubTree().InOrderTraversal()
        print(self)
        if self.GetRightSubTree() != None:
            self.GetRightSubTree().InOrderTraversal()
        return (True)

    def HasChildren(self):
        if self.GetChildren() == (None, None):
            return False
        return True

    def GetHeight(self):  # get height method that returns largest edges to the bottom leaf
        if self.GetChildren() == [None,
                                  None]:  # makes sure that a leaf node has height of 0 and others don't end up with + 1 of the actual height
            return 0
        x = 0
        y = 0
        if self.GetLeftSubTree() != None:
            x = self.GetLeftSubTree().GetHeight()
        if self.GetRightSubTree() != None:
            y = self.GetRightSubTree().GetHeight()
        return 1 + max(x, y)

    def SpecialSearch(self):  # find, return, and delete the rightmost leaf
        if self.GetRightSubTree() is not None:
            self.GetRightSubTree().SpecialSearch()
        if self.GetLeftSubTree() is not None:
            self.GetLeftSubTree().SpecialSearch()
        parent = self.GetParent()
        if parent.GetRightSubTree() == self:
            parent.SetRightSubTree(None)
        if parent.GetLeftSubTree() == self:
            parent.SetLeftSubTree(None)
        return self

    def Insert(self, n):
        if self.GetData() > n.GetData():
            if self.GetLeftSubTree() == None:
                self.SetLeftSubTree(n)
                n.SetParent(self)
                return
            return self.GetLeftSubTree().Insert(n)
        if self.GetData() < n.GetData():
            if self.GetRightSubTree() == None:
                self.SetRightSubTree(n)
                n.SetParent(self)
                return
            return self.GetRightSubTree().Insert(n)

    def Search(self, n):  # a binary search to find the matching node
        if self.GetData() > n.GetData():
            return self.GetLeftSubTree().Search(n)
        if self.GetData() < n.GetData():
            return self.GetRightSubTree().Search(n)
        return self


if (__name__ == "__main__"):
    print("in the main program")
    sampleNode = Node()
    print(sampleNode)
    secondNode = Node()
    secondNode.SetData(1)
    thirdNode = Node()
    thirdNode.SetData(3)
    secondNode.AddChildToTheLeft(thirdNode)
    thirdNode.SetData(4)
    secondNode.AddChildToTheRight(thirdNode)
    sampleNode.AddChildToTheLeft(secondNode)
    print(sampleNode)
    print(secondNode)
    print(secondNode)
    secondNode.SetData(2)
    sampleNode.AddChildToTheRight(secondNode)
    print("\nDFT")
    sampleNode.DepthFirstTraversal()
    print("\nIn-order traversal")
    sampleNode.InOrderTraversal()
    print(secondNode.GetHeight())
