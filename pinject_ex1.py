import pinject


class OuterClass(object):
    def __init__(self, inner_class):
        self.inner_class = inner_class


class InnerClass(object):
    def __init__(self):
        self.forty_two = 42


if __name__ == "__main__":
    obj_graph = pinject.new_object_graph()
    outer_class = obj_graph.provide(OuterClass)
    print(outer_class.inner_class.forty_two)

