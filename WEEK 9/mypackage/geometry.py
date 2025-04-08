PI = 3.14
class Circle:
    def __init__(self,at1):
        self.at1=at1
    def area(self):
        return PI*(self.at1 **2)
class Square:
    def __init__(self,at1):
        self.at1=at1
    def area(self):
        return (self.at1 **2)
class Rectangle:
    def __init__(self,at1, at2):
        self.at1=at1
        self.at2=at2
    def area(self):
        return (self.at1 * self.at2)