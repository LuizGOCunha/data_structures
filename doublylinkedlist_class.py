from typing import Union
from node_class import Node

class DoublyLinkedList:

    def __init__(self, root:Union[int, None]) -> None:
        self.root = Node(root)
        self.last = self.root
        self.size = 0

    def add(self, value:int):
        if self.size == 0:
            self.root = Node(value)
            self.last = self.root
        else:
            new_node = Node(value, next= self.root)
            self.root.previous = new_node
            self.root = new_node
        self.size += 1

    def find(self, value:int) -> Union[int, bool]:
        current = self.root
        while current is not None:
            if current.value == value:
                return current.value
            elif current == None:
                return False
            else:
                current = current.next

    def delete(self, value:int):
        current = self.root
        while current is not None:
            if current.value == value:
                if current.previous is not None:
                    if current.next is not None:
                        # Middle of the list
                        current.previous.next = current.next
                        current.next.previous = current.previous
                    else:
                        # End of the list
                        current.previous.next = None
                        self.last = current.previous
                else:
                    # Beginning of the list
                    current.next.previous = None
                    self.root = current.next
                # Found and removed
                self.size -= 1
                return True
            else:
                current = current.next
        # Not Found and not removed
        return False
    
    def print_list(self) -> None:
        if self.size == 0:
            return None
        else:
            current = self.root
            while current is not None:
                print(current, end="->")
                current = current.next
        print()

if __name__ == "__main__":
    x = DoublyLinkedList(1)
    for n in range(100):
        x.add(n)
    x.delete(99)
    x.print_list()
    print(x.find(33))
                
