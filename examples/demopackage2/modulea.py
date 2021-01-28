import abc

class IClassC(abc.ABC):
    @abc.abstractmethod
    def do_some_stuff(self):
        pass

class ClassA:
    def __init__(self):
        print("We instantiated from ClassA")

    def func_a(self, c: IClassC):
        print("Execution of func_a from ClassA")
        c.do_some_stuff()


