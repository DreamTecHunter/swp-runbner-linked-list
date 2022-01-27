class SimpleNode:
    def __init__(self, node=None):
        self.index = None
        self.node = node
        self.next_node = None


class SimpleLinkedList:
    def __init__(self):
        self.first_node = None

    def add(self):
        return

    def has_next(self):
        return

    def next(self):
        return

    def next_index(self):
        return

    def remove(self):
        return

    def set(self):
        return

    def to_string(self):
        return


if __name__ == '__main__':
    simple_linked_list = SimpleLinkedList()
    a = SimpleNode("A")
    b = SimpleNode("B")
    c = SimpleNode("C")
    simple_linked_list.first_node = a
    a.next_node = b
    b.next_node = c
    print("end")
