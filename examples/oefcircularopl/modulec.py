
class ClassC:
    def __init__(self):
        print("We instantiated from ClassC")

    def func_c(self, message, the_class):
        # the_class is injected
        print("func_c ", message)
        the_class.static_func_a("from ClassC")

