class full():
    def __init__(self, first, second, age):
        self.first = first
        self.second = second
        self.age = age
        self.email = first + "." + second + "@gmail.com"
    
    
    def myfunc(self):
        print(self.email)

    def myfunc2(self):
        pass

first = str(input())
second = str(input())
age = int(input())
p1 = full(first, second, age)
p1.myfunc()

