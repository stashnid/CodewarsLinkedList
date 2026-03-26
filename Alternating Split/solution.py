class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Розділяє список на два підсписки з елементів що чергуються."""
    if head is None or head.next is None:
        raise Exception("Error")

    first = head
    second = head.next
    
    f = first
    s = second
    
    while s and s.next:
        f.next = s.next
        f = f.next

        s.next = f.next
        s = s.next
        
    f.next = None
    
    if s:
        s.next = None

    return Context(first, second)