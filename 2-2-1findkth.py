import linkedlist

def FindKthElem(node, k):
    p1 = node
    p2 = node
    i = 0
    while i < k:
        p2 = p2.next
        i = i + 1
    while p2 != None:
        p1 = p1.next
        p2 = p2.next
    return p1

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(3)
l.insert(5)
n = FindKthElem(l.first,2)
print(n.value)
