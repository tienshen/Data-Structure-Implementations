# Author: Tien Li Shen
# 7/16/2019
# This homework will check on your engagement and understanding of stack and queues, as well as object oriented programming, data encapsulation, and information hiding.

# implement either a stack or a queue. The type of element you put into the stack or queue is up to you, it can be integers, or strings, or vehicles, or anything else. Make sure you implement all the member methods we covered in the course. You might want to  make reference to the course notes.
# if you implemented a stack in part 1, now implement a queue, but using only a stack. That is, do not make direct use of a python list. Instead, make use of one or more stacks to implement a queue.
# conversely, if you implemented a queue in part 1, now implement a stack, but using only a queue. That is, do not make direct use of a python list. Instead, make use of one or more queues to implement a stack.
# Obviously, the data structure you will implement in part 2 is not as efficient as that structure can be. This is just an exercise to check on your understanding of stacks, queues, object oriented programming, information hiding, and data encapsulation.

# I implemented the stack by using the sample code and added methods to it to complete it
class Stack:
    def __init__(self):
        self.storageList = []
        self.size = 0

    def Push(self, e):
        self.storageList.append(e)
        self.size = self.size + 1
        return (self.size)

    def Pop(self):
        valueToReturn = self.storageList.pop()
        self.size = self.size - 1
        return (valueToReturn)

    def Peek(self):
        return self.storageList[-1]

    def GetSize(self):
        return (self.size)

    def IsEmpty(self):
        if (self.size == 0):
            return (True)
        else:
            return (False)

# implementing stack with integers and using all the methods in the class
