from modulec import ClassC

class ClassB:
    def __init__(self):
        print("We instantiated from ClassB")
        self.c = ClassC()

    def func_b(self, message):
        print("func_b ", message)
        self.c.func_c("from ClassB")
