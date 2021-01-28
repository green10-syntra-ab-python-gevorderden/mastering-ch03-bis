
class ClassA:
    def __init__(self):
        print("We instantiated from ClassA")

    def func_a(self, c):
        print("Execution of func_a from ClassA")
        c.do_some_stuff()


