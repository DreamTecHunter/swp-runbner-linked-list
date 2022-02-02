from simpleLinkedList import *
import random


def simple_linked_list(min_range: int = 0, max_range: int = 10, size: int = 100):
    sll: SimpleLinkedList = SimpleLinkedList()
    for i in range(size):
        sll.add(random.randrange(start=min_range, stop=max_range, step=1))
    print("Address: %s" % sll)
    print("\tSize: %d" % sll.size())
    print("\tLast value: %d" % sll.get_last().element)
    print("\tToString: %s" % sll.to_string())


if __name__ == '__main__':
    simple_linked_list()