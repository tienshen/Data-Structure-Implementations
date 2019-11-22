# Author: Tien Li Shen
# 7/10/2019

class Vehicles:
    def __init__(self):
        self.passengers = 0
        self.wheels = 0
        self.name = None
        self.previous = None
        self.next = None

    def SetNumberOfPassengers(self, int):
        self.passengers = int

    def GetNumberOfPassengers(self):
        return self.passengers

    def SetNumberOfWheels(self, int):
        self.wheels = int

    def GetNumberOfWheels(self):
        return self.wheels

    def SetName(self, str):
        self.name = str

    def GetName(self):
        return self.name

    def __eq__(self, other): #this is the method that is related to the homework this week
        boo = False
        if self.GetName() == other.GetName():
            boo =  True
        return boo

class Bycicles(Vehicles):
    pass

if __name__ == '__main__':
    trek = Bycicles()
    trek.SetNumberOfPassengers(1)
    trek.SetNumberOfWheels(1)
    print(trek.GetNumberOfPassengers())
