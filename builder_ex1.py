""" @file builder_ex1.py """


class Simple(object):

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def print_values(self):
        print("a=%s, b=%s, c=%s" % (self.a, self.b, self.c))


class Builder(object):
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


# *************** TEST ****************
if __name__ == "__main__":
    s1 = Builder().with_a(11).with_b(22).with_c(33).simple
    s1.print_values()




