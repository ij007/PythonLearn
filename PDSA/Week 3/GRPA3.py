def reverse(root):
    prev = None
    curr = root
    while(curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev