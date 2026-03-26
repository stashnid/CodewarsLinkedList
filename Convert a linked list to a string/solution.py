class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """Повертає рядкове представлення списку у форматі '0 -> 1 -> None'."""
    parts = []
    probe = node
    while probe is not None:
        parts.append(str(probe.data))
        probe = probe.next
    if probe is None:
        parts.append('None')

    return " -> ".join(parts)

print(stringify(Node(0, Node(1, Node(2, Node(3))))))