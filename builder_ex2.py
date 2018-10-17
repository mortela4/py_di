""" @file builder_ex2.py """


class Simple(object):

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def print_values(self):
        print("a = no value" if self.a is None else "a = " + str(self.a))
        print("b = no value" if self.b is None else "b = " + str(self.b))
        print("c = no value" if self.c is None else "c =" + str(self.c))


class SimpleBuilder(object):
    def __init__(self):
        self.simple = Simple()

    def with_a(self, a):
        self.simple.a = a
        return self

    def with_b(self, b):
        self.simple.b = b
        return self

    def with_c(self, c):
        self.simple.c = c
        return self

    def build(self):
        return self.simple


# *************** TEST ****************
if __name__ == "__main__":
    s1 = SimpleBuilder().with_a(11).with_b(22).with_c(33).build()
    s1.print_values()
    s1.__dict__['b'] = 123
    s1.print_values()
    #
    s2 = SimpleBuilder().with_a(11).with_c(33).build()
    s2.print_values()
    s2.__dict__['b'] = 357
    s2.print_values()





