# -----------------------------Implementation-------------------------------------
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        print("a node is created with the value {0}".format(value))


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        print("-----new list is created-----")


list = LinkedList()
new = Node(200)
