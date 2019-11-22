# Tien Li Shen
# 7/24/2019
# Your task is to implement a doubly linked list, as an extension of the singly linked lists you can find in the course materials. You can also find more information on doubly linked lists in chapter 7 of our text book.
#
# Your implementation of a doubly linked list should include the following methids:
#
# an __init__ method
# an append(e) method, which adds element e to the end of the linked list.
# a len() method, which returns the current size of the linked list.
# an insert(e,i), which adds element e right before the ith element of the list. That is, the new element will now be in the ith position. If the linked list does not have i elements before the operation, the result is undefined.
# you can choose to provide an error message.
# or raise an exception
# or you can leave the situation unhandled, assuming that the user will check first
# a delete(i) method, which deletes the ith method from the linked list. This is where you will make the most important use of a pointer going from an element in the list to the previous element in the list. Pay attention to how to handle deleting the first element of the list, which is a valid operation. If the list doesn't have that many elements, the result of the operation is undefined.
# you can choose to provide an error message.
# or raise an exception
# or you can leave the situation unhandled, assuming that the user will check first.
# a method to return the ith element of the list, by creating a __getitem__ method.
# count(e,a), a method that counts how many times element e appears in the list. a is an optional parameter which defaults to zero.
# index(e,a) a method to search through part or all of the list, returning the index of the first occurrence of element e starting at position a. a should be an optional argument to the method. If it is not included in the method call, it should default to zero. That is, index(e) will look for element e through the whole linked list, starting with the element at position 0.
# these last two methods will require you to implement the __eq__ method, defining when two objects are equal.
# Your code should include a main program that tests the correctness of the methods implemented above.
# Your homework submission should include at least two files, one implementing the linked list, and another one implementing the vehicle class, or whatever class you choose to place into the linked list.

from Vehicles_linked import Vehicles


class LinkedList:
    def __init__(self):
        self.head = None  # first element in the list
        self.tail = None  # I made newest element to be the tail
        self.current = None
        self.size = 0

    def Append(self, e):
        # precondition  : e matches the format of the Record
        # postcondition : the new element is at the end of the linked list
        newElement = Vehicles()
        newElement.name = e.GetName()
        if self.size == 0:
            # this is the first element.
            #
            self.head = newElement
            self.tail = newElement
        else:
            # there are elements in the list already.
            # add this one at the end of the list.
            newElement.previous = self.tail
            newElement.previous.next = newElement  # this one totally tangled my mind
            self.tail = newElement
        self.size = self.size + 1
        return (self.tail)

    def DisplayAll(self):
        current = self.head
        print("Now printing linked list content:")
        print("\n")
        for i in range(self.size):
            name = current.GetName()
            print(name)
            current = current.next
        return (self.size)

    def Len(self):
        return (self.size)

    def Insert(self, e, i):  # insert also gave me a huge headache, figuring out how to make the arrows point to each other was a pain
        if i > self.size:  # if index exceeds size, methods needs to stop operation
            print("invalid index")
            return
        if i == self.size:  # if index indicates adding element to the end of the list, we can simply append the item
            self.Append(e)
            self.size = self.size + 1
            return
        if i == 0:
            self.head.previous = e
            e.next = self.head
            self.head = e
            self.size = self.size + 1
            return
        currentElement = self.head
        for x in range(i):
            currentElement = currentElement.next
        currentElement.previous.next = e
        e.next = currentElement
        e.previous = currentElement.previous
        currentElement.previous = e
        self.size = self.size + 1

    def Delete(self, i):
        # initial conditions
        if i >= self.size or i < 0:  # the working of the index caused a lot of confusion since its totally different comepre to isert and append
            print("invalid index")
            return
        if i == 0:
            self.head = self.head.next
            self.head.previous = None
            self.size = self.size - 1
            return
        if i == self.size - 1:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size = self.size - 1
            return
        current = self.head
        for x in range(i):
            current = current.next
        current.next.previous = current.previous  # looks pretty weird, not sure if it is right
        current.previous.next = current.next
        self.size = self.size - 1

    def __getitem__(self, i):
        current = self.head
        for x in range(i):
            current = current.next
        return current

    def Count(self, e, a=0):
        current = self.head
        for x in range(self.size):
            if e.__eq__(current):
                a = a + 1
            current = current.next
        return a


    def Index(self, e, a=0):
        current = self.head
        for x in range(self.size):
            if e.__eq__(current):
                return a
            current = current.next
            a = a + 1
        return "not found"

if __name__ == '__main__':
    #main program to run the code
    # I decided to use vehicles for this linked list and recycled a list from previous homeworks
    list = []
    list.append(Vehicles())
    list[-1].SetName("Bicycle")
    list[-1].SetNumberOfPassengers(1)
    list[-1].SetNumberOfWheels(2)

    # add code to add another object to the list, of class Vehicle, with name "passenger car", with four wheels and five passengers.
    list.append(Vehicles())
    list[-1].SetName("passenger car")
    list[-1].SetNumberOfPassengers(5)
    list[-1].SetNumberOfWheels(4)

    # add code to add another object to the list, of class Vehicle, with name "trailer", with 18 wheels a,d two passengers.
    list.append(Vehicles())
    list[-1].SetName("trailer")
    list[-1].SetNumberOfPassengers(2)
    list[-1].SetNumberOfWheels(18)

    list.append(Vehicles())
    list[-1].SetName("Bicycle")

    #now added all of the elements to the linked list with a for loop
    #also testing append 2
    sample_list = LinkedList()
    for i in range(len(list)):
        sample_list.Append(list[i])
    sample_list.DisplayAll()

    #testing
    item = Vehicles()
    item.SetName("StarShip")
    print("size of the linked list is: " +str(sample_list.Len()))

    #testing insert and delete, steps 4 and 5
    sample_list.Insert(item, 2)
    print("jaime added: all the list after inserting:")
    sample_list.DisplayAll()
    sample_list.Delete(1)
    sample_list.DisplayAll()

    #testing _getitem_, count, and index searchgin, steps 6, 7, and 8
    print("\n")
    print(sample_list.__getitem__(0).GetName())
    print("jaime added: printing a linked list element using indexes")
    print(sample_list[0].GetName())
    print("number of target vehicle: " + str(sample_list.Count(list[2])))
    print(sample_list.Index(list[1]))
