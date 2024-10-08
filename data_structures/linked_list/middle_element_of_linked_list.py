from __future__ import annotations

class Node:
    """Represents a node in the linked list."""
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class LinkedList:
    """Represents a linked list."""
    def __init__(self) -> None:
        self.head = None
        self.size = 0  # Keep track of the list size

    def push(self, new_data: int) -> None:
        """Adds a new node to the front of the list."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1  # Increment the list size

    def middle_element(self) -> int | None:
        """Returns the middle element of the list."""
        if not self.head:
            print("No element found.")
            return None

        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return slow_pointer.data

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return ' -> '.join(nodes)

if __name__ == "__main__":
    link = LinkedList()
    num_elements = int(input("Enter the number of elements: "))
    for _ in range(num_elements):
        data = int(input("Enter element {}: ".format(_ + 1)))
        link.push(data)
    print("Linked List:", link)
    print("Middle Element:", link.middle_element())
