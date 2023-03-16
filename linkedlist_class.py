from typing import Union

class Node:

    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"({self.value})"
    
class LinkedList:

    def __init__(self, root) -> None:
        self.root = Node(root)
        self.size = 0

    def add(self, value) -> None:
        new_node = Node(value, self.root)
        self.root = new_node
        self.size += 1

    def find(self, value) -> Union[Node, int]:
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return value
            else:
                current_node = current_node.next
        # Returns None if can't find value
        return None
    
    def remove(self, value) -> bool:
        current_node = self.root
        prev_node = None
        while current_node is not None:
            if current_node.value == value:
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    self.root = current_node.next
                self.size -= 1
                return True
            else:
                prev_node = current_node
                current_node = current_node.next
        # If didn't find something to remove, returns False
        return False
    
    def print_list(self) -> str:
        node = self.root
        while node is not None:
            print(node, end="->")
            node = node.next

if __name__ == "__main__":
    qw = LinkedList(1)
    for n in range(100):
        qw.add(n)
    breakpoint()

