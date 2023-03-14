from typing import Any

class Queue:
    '''Queues are data structures that are similar to Stacks, but obey a First In, First Out logic.
    This means it works in the same way as a line for a bank, let's say. 
    We have access to the first item to arrive, the last ones have to wait until we get to them.
    Real world uses of this structure can be seen in bank lines, restaurant orders, 
    supermarket checkouts, etc.'''

    def __init__(self) -> None:
        self.queue = list()
        
    def enqueue(self, item:Any) -> None:
        '''Put item in the end of the queue'''
        self.queue.append(item)

    def dequeue(self) -> Any:
        '''Take item from beginning of the queue and returns it'''
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
    
    def is_empty(self) -> bool:
        '''Checks if queue is empty'''
        if self.queue:
            return False
        else:
            return True
    
    def __str__(self) -> str:
        return str(self.queue)
    
qu = Queue()
breakpoint()