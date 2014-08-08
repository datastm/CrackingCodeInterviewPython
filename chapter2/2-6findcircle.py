import linkedlist

def FindCircle(llist):
    p1 = llist.first.next
    p2 = p1.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
    p1 = llist.first
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

l = linkedlist.LinkedList()
l.insert('A')
l.insert('B')
l.insert('C')
c = l.last
l.insert('D')
l.insert('E')
l.last.next = c
#l.PrintList()
print(FindCircle(l).value)
