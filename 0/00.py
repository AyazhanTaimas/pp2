class full:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def output_1(self):
        print(self.name + " "+ self.surname)

name = str(input())
surname = str(input())
p1 = full(name, surname)
p1.output_1()