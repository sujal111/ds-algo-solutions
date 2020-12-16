def reverse(head):  //Declaring the function(Head)
    
    if head is None:      //Traversing through the node and comparing
        return None
    prev = None
    curr = head
    aux = head.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = aux
        if curr is not None:
            aux = aux.next
    return prev