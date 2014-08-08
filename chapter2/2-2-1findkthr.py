import linkedlist

def FindKthElem(node, k):
    if node == None:
        return(None, 0)
    else:
        n,i = FindKthElem(node.next, k)
        if i == k:
            return(n, i)
        else:
            i = i + 1
    return(node, i)

l = linkedlist.LinkedList()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(3)
l.insert(5)
n, k = FindKthElem(l.first,4)
print(n.value)
