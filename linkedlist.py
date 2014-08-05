class Node():
    def __init__(self, data, n):
        self.value = data
        self.next = n

class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
    def insert(self, data):
        if self.first == None:
            self.first = Node(data, None)
            self.last = self.first
        else:
            cur_node = Node(data, None)
            self.last.next = cur_node
            self.last = cur_node
    def PrintList(self):
        p = self.first
        while p != None:
            print(p.value)
            p = p.next

