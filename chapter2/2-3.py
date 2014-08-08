import linkedlist

def DelNode(node):
    node.value = node.next.value
    node.next = node.next.next

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(3)
l.insert(5)
n = DelNode(l.first.next)
l.PrintList()
