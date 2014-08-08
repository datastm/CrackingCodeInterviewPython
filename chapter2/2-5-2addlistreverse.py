import linkedlist

def Len(l):
    p = l.first
    length = 0
    while p != None:
        length = length + 1
        p = p.next
    return length

def InsertT2H(l, data):
    new_node = linkedlist.Node(data, l.first)
    l.first = new_node
    return l

def PadList(llist,length):
    for i in range(0,length):
        InsertT2H(llist,0)
    return llist
    
def AddNode(n1, n2):
    if n1.next == None:
        s = linkedlist.LinkedList()
        value = n1.value + n2.value
        if value > 10:
            carry = 1
        else:
            carry = 0
        value = value % 10
        InsertT2H(s,value)
        return (s,carry)
    else:
        s,carry = AddNode(n1.next, n2.next)
        value = n1.value + n2.value + carry
        if value > 10:
            carry = 1
        else:
            carry = 0
        value = value % 10
        InsertT2H(s,value)
        return(s, carry)

def AddList(l1, l2):
    len1 = Len(l1)
    len2 = Len(l2)
    if len1 > len2:
        PadList(l2, len1 - len2)
    else:
        PadList(l1, len2 - len1)
    s,carry = AddNode(l1.first, l2.first)
    if carry == 1:
        InsertT2H(s,carry)
    return s

l1 = linkedlist.LinkedList()            
l2 = linkedlist.LinkedList()
l1.insert(6)
l1.insert(1)
l1.insert(7)
l2.insert(9)
l2.insert(5)
l3 = AddList(l1,l2)
l3.PrintList()
    
    
