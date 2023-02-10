class Square:
    def __init__(self, l = 0):
        self.l = l


class Shape(Square):
    def area(self):
        print(self.l ** 2)
        

class Rectangle:
    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht
        
class Shape2(Rectangle):
    def area(self):
        print(self.lenght * self.widht)
    
x = Shape(7)
x.area()
y = Shape2(5, 7)
y.area()