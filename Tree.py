# Author: Tien Li Shen
#
import copy

from Binary_node import Node


# Your task is to implement a binary search tree, which remains balanced under the operations of insertion and deletion. You can make use of the binary_node.py and the tree.py partial implementations that are posted on the blackboard site, as a starting point.

# Your tree should implement the following operations:
#   an init method.
#   an insert node method
#   a delete node method.
#   an in-order traversal method
#   it will probably be VERY useful for you to implement a restructure() method, like the one presented in code fragment 11.9 of our text book, which is also discussed in the notes presented in our class notes.
#   it will probably be very useful for you to implement a method that, given a node N, checks to see if the tree rooted at N is balanced.

# Your node should implement the following operations:
#   an init method
#   an operation to add a left subtree to a node.
#   an operation to add a right subtree to a node.
#   an operation that computes the height of a node. It can be recursive or non-recursive, but I recommend you implement a recursive version, so that you have some practice with that programming technique.
#   Many, if not all of the operations you have to present for a node have been either included in code available on blackboard, or on pseudo-code seen in class. You can choose to use those, or some of your own creation.

class Tree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def SetRoot(self, n):
        self.__root = copy.deepcopy(n)
        return (self.__root)

    def GetRoot(self):
        return (self.__root)

    def DepthFirstTraversal(self):
        print("\nTree traversal")
        if (self.GetRoot() == None):
            print("Tree is empty")
            return (False)
        else:
            return (self.GetRoot().DepthFirstTraversal())

    def InOrderTraversal(self):  # I wrote InOrderTraveral with the pseudo code from recursion notes
        if (self.GetRoot() == None):  # initial condition
            print("Tree is empty")
            return (False)
        self.GetRoot().InOrderTraversal()

    def Insert(self, n):  # insert with recursion, I used an extra variable parent to help me with recursion
        if self.GetRoot() == None:  # insert element as root if there is no root
            self.SetRoot(n)
            return
        self.GetRoot().Insert(n)
        self.__size += 1
        self.Restructure(n)
        return

    def Delete(self, n):  # I added an extra variable root to help me with recursion
        n = self.GetRoot().Search(
            n)  # I realized that the n I tried to delete is different from the one stored in the tree since the tree will have offsprings
        parent = n.GetParent()
        # in the case where n only has one or zero child, this works for both cases because if it's a leaf node, it will identify one side as None and set the node's parent's child to the other None
        if parent.GetData() > n.GetData():  # if node is smaller than parent #following code is the same for greater or smaller
            if n.GetLeftSubTree() == None:  # identify which subtree the child is in and change pointers
                parent.SetLeftSubTree(n.GetRightSubTree())
            if n.GetRightSubTree() == None:
                parent.SetLeftSubTree(n.GetLeftSubTree())
            n = None
            return
        else:  # if node is larger than parent
            if n.GetLeftSubTree() == None:  # identify which subtree the child is in and change pointers
                parent.SetRightSubTree(n.GetRightSubTree())
            if n.GetRightSubTree() == None:
                parent.SetRightSubTree(n.GetLeftSubTree())
            n = None
            return
        temp = n.GetLeftSubTree().SpecialSearch()  # I created a special search to help me find the rightmost node in the left subtree like the notes showed
        n.SetData(temp.GetData())  # replace data within node n to make it look like n was replaced

        return

    def Restructure(self, n):
        z = self.CheckTree(n)
        if z == None:
            return
        leftHeight = self.GetLeftSubTree().GetHeight()
        rightHeight = self.GetRightSubTree().GetHeight()
        x = z.GetLeftSubTree()  # 4 variables for 4 subtrees
        y = z.GetRightSubTree()
        w = None
        if leftHeight > rightHeight:  # rotate clockwise, I found a graph representation online to help me understand the transition and placements
            w = x.GetRightSubTree()
            z.SetParent(x)
            z.SetLeftSubTree(w)
            w.SetParent(z)
            x.SetParent(z.GetParent())
            x.SetRightSubTree(z)
        if leftHeight < rightHeight:  # rotate counter clockwise
            w = y.GetLeftSubTree()
            z.SetParent(y)
            z.SetRightSubTree(w)
            w.SetParent(z)
            y.SetParent(z.GetParent())
            y.SetLeftSubTree(z)

    def CheckTree(self, n):  # returns false if the tree is unbalanced
        leftHeight = 0
        rightHeight = 0
        if n.GetLeftSubTree() != None:
            leftHeight = n.GetLeftSubTree().GetHeight()
        if n.GetRightSubTree() != None:
            rightHeight = n.GetRightSubTree().GetHeight()
        if leftHeight - rightHeight > 1:
            return self
        if n == self.GetRoot():
            return None
        return self.CheckTree(n.GetParent())


# a main program to test the code
if (__name__ == "__main__"):
    print("in the main program")
    tree = Tree()
    node1 = Node()
    node1.SetData(4)
    tree.SetRoot(node1)
    #    print(tree.GetRoot())
    #    print("\ndepth first traversal")
    #    tree.DepthFirstTraversal()
    node2 = Node()
    node2.SetData(2)
    node3 = Node()
    node3.SetData(6)
    node4 = Node()
    node4.SetData(5)
    node5 = Node()
    node5.SetData(3)
    tree.Insert(node2)
    tree.Insert(node3)
    tree.Insert(node4)
    tree.Insert(node5)
    tree.Delete(node2)
    #   tree.DepthFirstTraversal()
    print("Jaime adds: here comes the inorder traversal")
    tree.InOrderTraversal()
    print("is the tree balanced?")
    print(tree.CheckTree(tree.GetRoot()))
