from .modulea import ClassA


class ClassB(ClassA):
    def __init__(self):
        print("We instantiated from ClassB")
        self.func_a()


class ClassC:
    def __init__(self):
        print("We instantiated from ClassC")

    def do_some_stuff(self):
        print("a cool object from class C, that's what I'am ")
