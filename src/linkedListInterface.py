class NodeInterface:
    pass


class LinkedListIterableInterface:
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def has_next(self):
        pass


class LinkedListInterface:
    def __iter__(self):
        pass

    def __is_element_index(self):
        pass

    def __node(self, index):
        pass

    def __rise_size(self):
        pass

    def __to_dict(self):
        pass

    def add(self, element: object):
        pass

    def check_element_index(self, index):
        pass

    def clear(self):
        pass

    def get(self, index: int):
        pass

    def get_last(self):
        pass

    def insert(self, index: int, element):
        pass

    def set(self, index: int, element):
        pass

    def size(self):
        pass

    def to_string(self):
        pass
