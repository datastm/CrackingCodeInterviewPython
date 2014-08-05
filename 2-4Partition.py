import linkedlist

def Partition(l, x):
    less = linkedlist.LinkedList()
    greater = linkedlist.LinkedList()
    p = l.first
    while p != None:
        if p.value < x:
            less.insert(p.value)
        else:
            greater.insert(p.value)
        p = p.next
    less.last.next = greater.first
    return less

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(3)
l.insert(5)
n = Partition(l,4)
n.PrintList()
