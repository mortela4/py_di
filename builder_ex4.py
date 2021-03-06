""" @file builder_ex4.py """


class SimpleA(object):

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def print_values(self):
        for field in self.__dict__:
            print(field + " = no value" if self.a is None else field + " = " + str(self.__dict__[field]))


class SimpleB(object):

    def __init__(self, a=None, c=None):
        self.a = a
        self.c = c

    def print_values(self):
        for field in self.__dict__:
            print(field + " = no value" if self.a is None else field + " = " + str(self.__dict__[field]))


class GenericBuilder(object):
    def __init__(self, class_type):
        self.co = class_type()

    def with_field(self, field_name, value):
        self.co.__dict__[field_name] = value
        if field_name not in self.co.__dict__:
            print("Warning: field named '%s' - not in class! Extending class ..." % field_name)
        return self

    def build(self):
        return self.co


# *************** TEST ****************
if __name__ == "__main__":
    print("Test 1a:")
    s1 = GenericBuilder(SimpleA).with_field('a', 11).with_field('b', 22).with_field('c', 33).build()
    s1.print_values()
    print("Test 1b:")
    s1.__dict__['b'] = 123
    s1.print_values()
    #
    print("Test 2a:")
    s2 = GenericBuilder(SimpleB).with_field('a', 11).with_field('b', -99).with_field('c', 33).build()
    s2.print_values()
    print("Test 2b:")
    s2.__dict__['c'] = 357
    s2.print_values()
    print("Test 2c:")
    s2.__dict__['d'] = -777  # No warning - class is simply extended ...
    s2.print_values()
    print("Test 3:")
    s3 = GenericBuilder(SimpleB).with_field('d', 11).with_field('e', -99).with_field('f', 33).build()
    s3.print_values()





