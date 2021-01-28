from modulec import ClassC

class ClassB:
    def __init__(self):
        print("We instantiated from ClassB")
        self.c = ClassC()

    def func_b(self, message, the_class):
        # the_class is injected
        print("func_b ", message)
        self.c.func_c("from ClassB", the_class)
