class size_str:
    def input_1(self, word):
        self.word = word
    
    def output_1(self):
        print(len(self.word))

word = input()
p1 = size_str()
p1.input_1(word)

p1.output_1()