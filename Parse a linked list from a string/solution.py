class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """Створює однозв'язний список з рядка формату '1 -> 2 -> 3 -> None'."""
    parts = list_repr.split(" -> ")
    node = None
    
    for part in reversed(parts):
        if part in ('null', 'None'):
            continue
        node = Node(int(part), node)

    return node