import array as arr


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.priority = 0


class Queue:
    numArray = arr.array(20)

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new):
        print("enqueue function is called")
        if self.front is None:

            self.front = new
            self.rear = new
        else:

            self.rear.next = new
            self.rear = new

    def dequeue(self):

        if self.front is None:
            print("No data in Queue.")
        else:
            temp = self.front
            self.front = temp.next
        retun
        temp
        del temp

    def insertTo_array(element, value):
        numArray[element] = value

    def show_array():
        for i in range(0, 19):
            print(numArray[i])


newQueue = Queue()
for i in range(0, 19):
    bilAmount = int(input("Enter bill amount:"))
    NewNode = Node(bilAmount)
    newQueue.enqueue(NewNode)
for j in rage(0, 19):
    result = dequeue(newQueue)
    if j < 10:
        dis = result * 0.05
        insertTo_array(j, dis)
    else:
        insertTo_array(j, result)
show_array()
