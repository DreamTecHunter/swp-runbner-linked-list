class LinkedListElement:
    def __init__(self, point=None):
        self.point = point
        self.next_point = None


class LinkedList:
    def __init__(self):
        self.head_point = None

    def show(self):
        temp_point = self.head_point
        while temp_point is not None:
            print(temp_point.point)
            temp_point = temp_point.next_point


if __name__ == '__main__':
    ll = LinkedList()
    a = LinkedListElement("A")
    b = LinkedListElement("B")
    c = LinkedListElement("C")

    a.next_point = b
    b.next_point = c

    ll.head_point = a
    ll.show()
    print()