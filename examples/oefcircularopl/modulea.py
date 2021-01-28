from moduleb import ClassB

class ClassA:
    def __init__(self):
        print("We instantiated from ClassA")
        self.b = ClassB()

    @staticmethod
    def static_func_a(message):
        print("static func_a ", message)

    def func_a(self, message):
        print("func_a ", message)
        self.b.func_b("from ClassA",self.__class__)


a = ClassA()
a.func_a("from Main")