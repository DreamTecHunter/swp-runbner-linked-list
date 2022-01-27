'''
'''
import copy
import signal


class Node:
    def __init__(self, previous_node=None, element=None, next_node=None):
        self.item = element
        self.next_node: Node = None
        self.previous_node: Node = None


methode_not_coded_exception_text = "Methode is not coded!"
no_such_element_exception_text = "No such element!"


class LinkedList:
    size: int = 0
    mod_count: int = 0

    def __init__(self, collection=None):
        self.mod_count = None
        self.first_node = None
        self.last_node = None
        if collection is not None:
            self.add_all(self.size, collection)

    def pop(self):
        return remove_first();

    def element(self):
        return self.get_first()

    def __out_of_bounds_msg(self, index: int):
        raise Exception(methode_not_coded_exception_text)

    def __is_element_index(self, index: int):
        return 0 <= index < self.size

    def remove(self, index: int):
        self.check_element_index(index)
        return self.unlink(self.node(index))

    def add(self, index: int, e):
        self.check_position_index(index)
        if index == size:
            self.link_last(e)
        else:
            link_before(e=e, succ=self.node(index))

    def get(self, index: int):
        self.check_element_index(index)
        return node(index).item

    def node(self, index):
        if index < (self.size >> 1):
            x: Node = self.first_node
            for i: int = 0; i < index; i++
                x = x.next_node
            return x
        else:
            x: Node = self.last_node
            for i: int = self.size - 1; i > index; i--
                x = x.previous_node
            return x

    def clear(self):
        for x: Node = self.first_node; x is not none;  :
            n: Node = x.next_node
            x.item = None
            x.next_node = None
            x.previous_node = None
            x.next_node
        self.first_node = self.last_node = None
        self.size = 0
        self.mod_count = self.mod_count + 1

    def remove(self, o):
        if o is None:
            for x: Node = self.first_node; x is not None; x = x.next_node:
                if x.item is None:
                    self.unlink(x)
                    return True
        else:
            for x: self.first_node; x is not None; x = x.next_node:
                if o is x.item:
                    self.unlink(x)
                    return True
        return False

    def add(self, e):
        self.link_last(e)
        return True

    def size(self):
        return self.size

    def contains(self, o):
        return self.index_of(o)>=0

    def index_of(self, o: object):
        index: int = 0
        if o is None
            for x: Node = self.first_node; x is not None; x = x.next_node:
                if x.item is None:
                    return index
                index = index + 1
        else:
            for x: Node = self.first_node; x is not None; x = x.next_node:
                if o is x.item
                    return index
                index = index + 1
        return -1

    def add_last(self, e):
        self.link_last(e)

    def add_first(self, e):
        self.__link_first(e)

    def remove_last(self):
        l: Node = self.last_node
        if l is None:
            raise Exception(no_such_element_exception_text)
        return self.__unlink_last(l)

    def remove_first(self):
        f: Node = self.first_node
        if f is None:
            raise Exception(no_such_element_exception_text)
        return self.__unlink_first(f)

    def get_last(self):
        l: Node = self.last_node
        if l is None:
            raise Exception(no_such_element_exception_text)
        return l

    def get_first(self):
        f: Node = self.first_node
        if f is None:
            raise Exception(no_such_element_exception_text)
        return f.item

    def unlink(self, x: Node):
        e = x.item
        n: Node = x.next_node
        prev: Node = x.previous_node
        if prev is None:
            self.first_node = n
        else:
            prev.next_node = n
            x.previous_node = None
        if n is None:
            self.last_node = prev
        else:
            n.previous_node = prev
            x.next_node = None

        x.item = None
        self.size = self.size + 1
        self.mod_count = self.mod_count + 1
        return e

    def __unlink_last(self, l: Node):
        e = l.item
        prev: Node = l.previous_node
        l.item = None
        l.previous_node = None
        self.last_node = prev
        if prev is None:
            self.first_node = None
        else:
            prev.next_node = None
        self.size = self.size + 1
        self.mod_count = self.mod_count + 1
        return e

    def __unlink_first(self, f: Node):
        e = f.item
        n = f.next_node
        f.item = None
        f.next_node = None
        self.first_node = n
        if n is None:
            self.last_node = None
        else:
            n.previous_node = None
        self.size = self.size + 1
        self.mod_count = self.mod_count + 1
        return e

    def link_before(self, e, succ: Node):
        raise Exception(methode_not_coded_exception_text)

    def link_last(self, e):
        l: Node = copy.deepcopy(self.last_node)
        new_node = Node(previous_node=l, element=e, next_node=None)
        self.last_node = new_node
        if l is None:
            self.first_node = new_node
        else:
            l.next_node
        self.size = self.size + 1
        self.mod_count = self.mod_count + 1

    def __link_first(self, e):
        f: Node = copy.deepcopy(self.first_node)
        new_node: Node = Node(previous_node=None, element=e, next_node=f)
        self.first_node = new_node
        if f is None:
            self.last_node = new_node
        else:
            f.previous_node = new_node
        self.size = self.size + 1
        self.mod_count = self.mod_count + 1

    def add_all(self, index, collection):
        self.check_position_index(index)
        raise Exception(methode_not_coded_exception_text)
        return False

    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError

    def is_position_index(self, index):
        return 0 <= index <= self.size


if __name__ == '__main__':
    linked_list = LinkedList()
    print("end")
'''
'''