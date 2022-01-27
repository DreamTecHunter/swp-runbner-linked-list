import copy

class SingleLinkedListElement:
    def __init__(self, point=None):
        self.point = point
        self.next_point = None


class DualLinkedListElement:
    def __init__(self, point=None):
        self.before_point = None
        self.point = point
        self.next_point = None


class SingleLinkedList:
    def __init__(self):
        self.single_linked_element

    def next(self):
        return


class DualLinkedList:
    size = 0

    def __init__(self):
        self.dual_linked_element = None

    def has_next(self):
        return self.dual_linked_list.next_point is not None

    def next(self):
        self.dual_linked_element = self.dual_linked_element.next_point

    def before(self):
        self.dual_linked_element = self.dual_linked_element.before_point

    def add(self, element):
        if self.dual_linked_element is None:
            self.dual_linked_element = element
            return
        temp_element = self.dual_linked_element
        while temp_element is not None:
            temp_element = temp_element.next_point
        temp_element.next_point = DualLinkedListElement(element)
        self.size = self.size + 1


if __name__ == '__main__':
    dual_linked_list = DualLinkedList()
    dual_linked_list.add("1.LOL")
    dual_linked_list.add("2.WOW")
    print(dual_linked_list.size)
    print(dual_linked_list)
