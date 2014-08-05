class Node():
    def __init__(self, data, n):
        self.value = data
        self.next = n

class Stack():
    def __init__(self):
        self.top = None
    def pop(self):
        temp = self.top
        self.top = temp.next
        return temp
    def push(self, data):
        temp = self.top
        self.top = Node(data,temp)
    def peek(self):
        return self.top.value
    def isEmpty(self):
        if self.top == None:
            return True
        return False
    
        
