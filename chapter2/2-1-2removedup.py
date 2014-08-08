import linkedlist

def DeleteDups(h):
    p1 = h.first
    while p1 != None:
        p2 = p1.next
        t = p1
        while p2 != None:
            if p2.value == p1.value:
                t.next = p2.next
            else:
                t = p2
            p2 = p2.next
        p1 = p1.next
            

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(1)
l.insert(3)
l.insert(3)
l.PrintList()

DeleteDups(l)
l.PrintList()
