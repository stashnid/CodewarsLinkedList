class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """Видаляє дублікати з відсортованого списку."""
    probe = head
    while probe and probe.next:
        if probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head