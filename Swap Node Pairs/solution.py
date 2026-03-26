class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """Міняє місцями кожну пару сусідніх вузлів."""
    node = Node()
    node.next = head
    probe = node
    while probe.next and probe.next.next:
        first = probe.next
        second = probe.next.next

        first.next = second.next
        second.next = first

        probe.next = second

        probe = first

    return node.next