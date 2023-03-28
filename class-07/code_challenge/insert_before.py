# LL: (1) -> (3) -> (2) -> None
#             ^
# 3, 5 Before the 3, insert the 5
# LL: (1) -> (5) -> (3) -> (2) -> (3)-> None
def insert_before(self, value_before, node_to_add):
    current = self.head # This assigns the current value to the head node
    while current:
        if current.value == value_before:
            node = Node(node_to_add, current)
            previous.next = node
            break

        previous = current
        current = current.next
