from .moduleb import ClassC


class ClassA:
    def __init__(self):
        print("We instantiated from ClassA")

    def func_a(self):
        print("Execution of func_a from ClassA")
        c = ClassC()
        c.do_some_stuff()