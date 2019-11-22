# Author: Tien Li Shen
# 7/10/2019

class Vehicles:
    def __init__(self):
        self.passengers = 0
        self.wheels = 0
        self.name = ""

    def SetNumberOfPassengers(self, int):
        self.passengers = int

    def GetNumberOfPassengers(self):
        return self.passengers

    def SetNumberOfWheels(self, int):
        self.wheels = int

    def GetNumberOfWheels(self):
        return self.wheels

    # Week1 assignment
    def SetName(self, str):
        self.name = str

    def GetName(self):
        return self.name

if __name__ == '__main__':

    # Create an empty list.
    # add code to add, to this list, an object of class Vehicle, with name "Bicycle", with two wheels and one passenger.
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

    # add code that displays all three elements currently in the list.
    print("elements in the list:")
    for x in range(len(list)):
        print(list[x].GetName())

    # add code that returns the index, inside the list, for an object with name "Bicycle". Change the number of passengers for that vehicle from one to two.
    for i in range(len(list)):
        if list[i].GetName() == ("Bicycle"):
            print("indx of Bicycle: " + str(i))
            list[i].SetNumberOfPassengers(2)

    # add code that returns the index, inside the list, for an object with name "trailer". Delete that element from the list.
    for i in range(len(list)):
        if list[i].GetName() == ("trailer"):
            print("index of Trailer: " + str(i))
            del list[i]

    # add code to insert an element of type Vehicle to the list. This vehicle will have name "School bus", with eight wheels and 30 passengers. Add this element between the two Vehicles that are currently in the list.
    #list.append(Vehicles())
    #list[-1].SetName("School Bus")
    #list[-1].SetNumberOfPassengers(30)
    #list[-1].SetNumberOfWheels(8)
    list.insert(1, Vehicles())
    list[1].SetName("School Bus")
    list[1].SetNumberOfPassengers(30)
    list[1].SetNumberOfWheels(8)

    # add code that displays all elements of the list at this point.
    print("elements in the list:")
    for i in range(len(list)):
        print(list[i].GetName())
