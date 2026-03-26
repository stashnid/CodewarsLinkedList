class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    """Вставляє новий вузол у відсортований список"""
    node = Node(data)
    if head is None or data <= head.data:
        node.next = head
        return node
    
    probe = head
    while probe.next is not None and probe.next.data < data:
        probe = probe.next

    node.next = probe.next
    probe.next = node
    
    return head