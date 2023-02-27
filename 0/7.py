class my_class:
    def __init__(self, str1):
        self.str1 = str1

    def output_1(self):
        print(len(str1))

str1 = str(input())
p = my_class(str1)
p.output_1()