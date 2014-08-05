import linkedlist

def reverse(node):
    if node == None:
        rev = linkedlist.LinkedList()
        return rev
    else:
        rev = reverse(node.next)
        rev.insert(node.value)
    return rev

def checkPLD(llist):
    flag = True
    p1 = llist.first
    p2 = reverse(llist.first).first
    while p1 != None:
        if p1.value != p2.value:
            flag = False
        p1 = p1.next
        p2 = p2.next
    return flag

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(2)
l.insert(1)
print(checkPLD(l))
