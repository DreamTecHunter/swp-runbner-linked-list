import json


class SimpleNode:
    def __init__(self, element: object = None, next_node=None):
        self.element = element
        self.next_node = next_node


class SimpleLinkedListIterable:
    def __init__(self, simple_linked_list):
        self.__simple_linked_list = simple_linked_list
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < self.__simple_linked_list.size():
            result = self.__simple_linked_list.get(self.__index)
            self.__index += 1
            return result
        raise StopIteration

    def has_next(self):
        return self.__index < self.__simple_linked_list.size()


class SimpleLinkedList:
    def __init__(self):
        self.__first_node: SimpleNode = None
        self.__size = 0

    def __iter__(self):
        return SimpleLinkedListIterable(self)

    def __is_element_index(self, index):
        return 0 <= index < self.__size

    def __node(self, index):
        if self.__is_element_index(index):
            x: SimpleNode = self.__first_node
            i = 0
            while i < index:
                x = x.next_node
                i += 1
            return x

    def __rise_size(self):
        self.__size += 1

    # TODO: Methode misses an key-value for the value-key
    def __to_dict(self):
        raise Exception("Cannot convert to dictionary")
        return json.loads(self.to_string())

    def add(self, element: object):
        if self.get_last() is None:
            self.__first_node = SimpleNode(element)
        else:
            self.get_last().next_node = SimpleNode(element)
        self.__rise_size()

    def check_element_index(self, index):
        if not self.__is_element_index(index):
            raise IndexError(index)

    def clear(self):
        self.__first_node = None
        self.__size = 0

    def get(self, index: int):
        self.check_element_index(index)
        return self.__node(index).element

    def get_last(self):
        if self.__first_node is None:
            return None
        else:
            node: SimpleNode = self.__first_node
            while node.next_node is not None:
                node = node.next_node
            return node

    def insert(self, index: int, element):
        self.check_element_index(index)
        if index is self.__size:
            self.add(element)
        else:
            new_node = SimpleNode(element)
            new_node.next_node = self.__node(index)
            if index == 0:
                self.__first_node = new_node
            else:
                self.__node(index - 1).next_node = new_node

    def set(self, index: int, element):
        to_be_inserted_node: SimpleNode = SimpleNode(element)
        if index == self.size():
            self.add(element)
        elif index == 0:
            to_be_inserted_node.next_node = self.__node(0).next_node
            self.__first_node = to_be_inserted_node
        else:
            self.check_element_index(index)
            to_be_inserted_node.next_node = self.__node(index).next_node
            self.__node(index - 1).next_node = to_be_inserted_node

    def size(self):
        return self.__size

    def to_string(self):
        result = "{size:%d, values:{" % self.__size
        try:
            iterator = self.__iter__()
            while iterator.has_next():
                result += "%s" % iterator.__next__() + (", " if iterator.has_next() else "}}")
        except StopIteration:
            print("Iterator tried to iterate non-existing element")
        except:
            print("Something happened while iterating")
        """
        for value in self.__iter__():
            result += ", %s" % value
        """
        return result
