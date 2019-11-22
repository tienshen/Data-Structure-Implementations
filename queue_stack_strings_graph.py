# Author: Tien Li Shen
# 7/16/2019
# This homework will check on your engagement and understanding of stack and queues, as well as object oriented programming, data encapsulation, and information hiding.

# implement either a stack or a queue. The type of element you put into the stack or queue is up to you, it can be integers, or strings, or vehicles, or anything else. Make sure you implement all the member methods we covered in the course. You might want to  make reference to the course notes.
# if you implemented a stack in part 1, now implement a queue, but using only a stack. That is, do not make direct use of a python list. Instead, make use of one or more stacks to implement a queue.
# conversely, if you implemented a queue in part 1, now implement a stack, but using only a queue. That is, do not make direct use of a python list. Instead, make use of one or more queues to implement a stack.
# Obviously, the data structure you will implement in part 2 is not as efficient as that structure can be. This is just an exercise to check on your understanding of stacks, queues, object oriented programming, information hiding, and data encapsulation.

from Stack_integer_graph import Stack


class Queue(Stack):
    def __init__(self):
        self.storageStack = Stack()
        self.size = 0

    # I edited enqueue to use stack.push
    def Enqueue(self, e):
        self.storageStack.Push(e)
        self.size = self.storageStack.GetSize()
        return (self.storageStack.GetSize())

    # for dequeue, I could not just use stack.pop. because that would be poping the top value
    # instead, I accessed the list within stack to delete the first value
    def Dequeue(self):
        tempList = Stack()  # a temporary stack to hold value from storageStack
        for x in range(
                self.storageStack.GetSize()):  # put all of the elements in storage into templist in the opposite order
            tempList.Push(self.storageStack.Pop())
        valueToReturn = tempList.Pop()  # the top element in tempList is the bottom element of storageStack. when we pop that it is essentially dequeueing storageStack
        for x in range(tempList.GetSize()):  # use this for loop to fill storage list with the new list after dequeueing
            self.storageStack.Push(tempList.Pop())
        self.size = self.storageStack.GetSize()
        return (valueToReturn)  # return the element that got popped
