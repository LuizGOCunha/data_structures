# This allows us to make the annotation that next and previous are also Nodes
from __future__ import annotations

class Node:

    def __init__(self, value:int, next:Node=None, previous:Node=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self) -> str:
        return f"({self.value})"