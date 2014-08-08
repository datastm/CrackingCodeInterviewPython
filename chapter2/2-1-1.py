import linkedlist

def DeleteDups(h):
    p = h.first
    t = None
    table = {}
    while p != None:
        if(p.value in table):
            t.next = p.next
        else:
            t = p
            table.update({t.value:1})
        p = p.next
            

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(1)
l.insert(3)
l.insert(3)
l.PrintList()

DeleteDups(l)
l.PrintList()
