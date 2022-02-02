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
