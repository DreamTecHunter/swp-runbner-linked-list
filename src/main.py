from simpleLinkedList import *

if __name__ == '__main__':
    sll: SimpleLinkedList = SimpleLinkedList()
    sll.add(1)
    sll.add(2)
    sll.add(4)
    print(sll.size())
    print(sll.get_last().item)
    print(sll.get(2))
    for value in sll:
        print(value)
    print(sll.to_string())
    print(sll.to_json())
    sll.clear()
    print(sll.size())

