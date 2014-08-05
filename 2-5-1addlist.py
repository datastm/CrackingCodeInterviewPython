import linkedlist

def AddNum(l1, l2):
    sum = linkedlist.LinkedList()
    p1 = l1.first
    p2 = l2.first
    carry = 0
    while p1 != None or p2 != None:
        p = carry
        if p1 != None:
            p = p1.value + p
            p1 = p1.next
        if p2 != None:
            p = p2.value + p
            p2 = p2.next
        if p > 10:
            carry = 1
        else:
            carry = 0
        p = p % 10
        sum.insert(p)
    return sum
        

l1 = linkedlist.LinkedList()            
l2 = linkedlist.LinkedList()
l1.insert(7)
l1.insert(1)
l1.insert(6)
l2.insert(5)
l2.insert(9)
l3 = AddNum(l1,l2)
l3.PrintList()
