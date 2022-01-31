# Tis is the Node structure/Class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        print("-----new node is created with value {0}-----".format(self.data))


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        print("-----new list is created-----")

    # --------Interface---------------
    def insert_begining(self, new):
        print("insert begining function is called")
        if self.head is None:
            print("head was null and new node inserted to front")
            self.head = new
            self.tail = new
        else:
            print("there was node/head is not null, and new node inserted to front")
            new.next = self.head
            self.head = new

    def insert_end(self, new):
        print("insert end function is called")
        if self.head is None:
            print("head was null and new node inserted to end(that is to the front)")
            self.head = new
            self.tail = new
        else:
            print("there was node/head is not null, and new node inserted to end")
            self.tail.next = new
            self.tail = new

    def insert_after(self, new, searchValue):
        print("insert after function is called")
        if self.head is None:
            print("No data in LL. So cannot insert after the given value")
        else:
            temp = self.head
            while temp is not None:
                if temp.data is searchValue:
                    break
                else:
                    temp = temp.next
            new.next = temp.next
            temp.next = new

    def delete(self, deleteValue):
        print("delete function is called")
        if self.head is None:
            print("No data in LL. So cannot delete the given value")
        else:
            temp = self.head
            temp1 = temp
            while temp is not None:
                if temp.data is deleteValue:
                    break
                else:
                    temp1 = temp
                    temp = temp.next
            if temp == temp1:
                self.head = temp.next
                del temp
            else:
                temp1.next = temp.next
                del temp

    def traverse_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next


list = LinkedList()
NewNode = Node(20)
list.insert_begining(NewNode)
NewNode = Node(15)
list.insert_begining(NewNode)
NewNode = Node(5)
list.insert_end(NewNode)
NewNode = Node(100)
list.insert_after(NewNode, 15)
NewNode = Node(200)
list.insert_after(NewNode, 100)
NewNode = Node(99)
list.insert_after(NewNode, 20)
list.traverse_list()
list.delete(100)
list.traverse_list()
list.delete(15)
list.traverse_list()
