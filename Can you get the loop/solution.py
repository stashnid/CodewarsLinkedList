class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    """Повертає довжину циклу в зв'язному списку."""
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    fast = fast.next

    while fast != slow:
        fast = fast.next

        count += 1

    return count