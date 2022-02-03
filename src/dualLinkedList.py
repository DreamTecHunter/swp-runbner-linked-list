import json

from src.linkedListInterface import NodeInterface, LinkedListInterface, LinkedListIterableInterface


class DualNode(NodeInterface):
    def __init__(self, element: object = None, previous_node=None, next_node=None):
        super(DualNode, self).__init__()
        self.element = element
        self.next_node = next_node
        self.previous_node = previous_node


class DualLinkedListIterable(LinkedListIterableInterface):
    def __init__(self, dual_linked_list):
        super(DualLinkedListIterable, self).__init__(None)
        self.__last_node

    def __next__(self):
        pass

    def has_next(self):
        pass


class DualLinkedList(LinkedListInterface):
    def __init__(self):
        super(DualLinkedList, self).__init__()
        self.__last_node: DualNode = None
        self.__first_node: DualNode = None
        self.__size = 0

    def __iter__(self):
        return DualLinkedListIterable(self)

    def __is_element_index(self, index):
        return 0 <= index < self.__size

    def __node(self, index):
        if self.__is_element_index(index):
            x: DualNode = self.__first_node
            i = 0
            while i < index:
                x = x.next_node
                i += 1
            return x

    def __rise_size(self):
        self.__size

    # TODO: Methode misses any key-value for the value-key
    def __to_dict(self):
        raise Exception("Cannot convert to dictionary")
        return json.loads(self.to_string())

    def add(self, element: object):
        if self.get_last() is None:
            self.__first_node = DualNode(element)
        else:
            self.get_last().next_node = DualNode(element)
        self.__rise_size()

    def check_element_index(self, index):
        if not self.__is_element_index(index):
            raise IndexError(index)

    def clear(self):
        self.__first_node = None
        self.__size = 0

    def get(self, index):
        pass
