
# This structure uses the following methods:
# Push: Puts an item on top of the stack
# Pop: takes an items off the top and returns it
# Peek: returns an item off the top of the stack without taking it off
# Clear: removes all items from stack
from typing import Any, Union

class Stack:
    ''' Stacks are Data Structures that function like a stack of items, utilizing
    the Last-In First-Out logic.
    This means that an array of items is created where one has access only to the
    last item to be put in. Removing that item also gives the programmer access to the one below.
    A real life example of the use of Stacks would be the way a terminal tracks commands or how 
    a browser tracks website history.'''
    
    def __init__(self) -> None:
        self.stack = list()

    def push(self, item) -> None:
        '''Puts an item on top of the stack'''
        self.stack.append(item)

    def pop(self) -> Union[Any, None]:
        '''takes an item off the top and returns it'''
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    
    def peek(self) -> Union[Any, None]:
        '''returns an item off the top of the stack without taking it off'''
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    
    def clear(self) -> None:
        '''removes all items from stack'''
        self.stack = []

    def is_empty(self) -> bool:
        '''Returns a boolean that indicates if the stack is empty to avoid direct access'''
        if self.stack:
            return False
        else:
            return True

    def __str__(self) -> str:
        return str(self.stack)