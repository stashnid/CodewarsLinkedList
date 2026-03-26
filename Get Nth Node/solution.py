class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

def get_nth(node, index):
    """Повертає вузол за індексом."""
    if node is None or index < 0:
        raise Exception("Invalid index")

    probe = node
    for _ in range(index):
        if probe.next is None:
            raise Exception("Invalid index")
        probe = probe.next
    
    return probe