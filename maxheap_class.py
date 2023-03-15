from typing import Any, Tuple, Union
from copy import copy

class MaxHeap:
    '''A MaxHeap is a data structure that grows in the shape of a pyramid, each node on the heap
    can have two child nodes that should have smaller values, and each can have one parent that
    should have a greater value. This data structure can be used for when you want easy access to
    the maximum value inside an array, because the maximum value will always stay as index 1.'''
    def __init__(self,*items:int) -> None:
        self.heap = list(items)
        # insert the 0 value in the first column to make it a 1 based heap
        self.heap.insert(0,0)
        # organize the heap
        self.organize_heap()

    def organize_heap(self):
        '''A useful method that allows us to float_up all indexes to its appropriate position.'''
        for index, _ in enumerate(self.heap):
            self.float_up(index)

    def swap(self, index1:int, index2:int) -> None:
        '''A method created so we can easily swap two items in the heap'''
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def parent(self, index:int) -> Union[int, None]:
        '''Returns the parent of a given node. If node is on top of the heap, returns None'''
        parent = index//2
        if parent == 0:
            return None
        else:
            return parent 

    def children(self, index:int) -> Tuple[int, None]:
        '''Returns the children of a node ,if children exist. If children do not exist,
        returns None for all non existant children.'''
        child_l = index*2
        child_r = index*2+1
        last_index = len(self.heap) - 1
        if child_l > last_index:
            return None, None
        elif child_r > last_index:
            return child_l, None
        else:
            return child_l, child_r
    
    # Should it always use the last index?
    # R: No because we are using recursion, remember?
    def float_up(self, index:int) -> None:
        '''A recursive method that receives an index (always initiated by last index), then checks
        if it is bigger than its parent. If it is bigger, trades places and calls itself on its new
        location. If not, returns None and ends operation. 
        Final result: item on the last index is put in its adequate place inside the heap.'''
        parent_i = self.parent(index)
        if parent_i == None:
            return None
        bigger_than_parent = self.heap[index] > self.heap[parent_i] 
        if bigger_than_parent:
            self.swap(index, parent_i)
            return self.float_up(parent_i)
        
    def bubble_down(self, index:int) -> None:
        '''The inverse process as the float up. This is a recursive method that receives an index (always
        initiated by index 1), then checks if it is smaller than any of its children. If its smaller than one 
        child, trades places with that child. If its smaller than both children, trades place with the one with
        the biggest value. If it is not smaller than its children or if it has no children, ends the process.'''
        child_l, child_r = self.children(index)
        biggest_index = index
        if child_l is not None:
            if self.heap[child_l] > self.heap[biggest_index]:
                biggest_index = child_l
        if child_r is not None:
            if self.heap[child_r] > self.heap[biggest_index]:
                biggest_index = child_r
        if biggest_index != index:
            self.swap(biggest_index, index)
            return self.bubble_down(biggest_index)
        
    def last_index(self) -> int:
        '''Method that returns the last index of our heap.'''
        return len(self.heap) -1
        
    def push(self, value:str) -> None:
        '''A method that append a value to the end of our heap, than bubble it up to its 
        appropriate position.'''
        self.heap.append(value)
        self.float_up(self.last_index())

    def peek(self) -> int:
        '''Returns the value at the top of the heap.'''
        return self.heap[1]
    
    def is_empty(self) -> bool:
        '''Useful method to check if the list is empty'''
        if len(self.heap) == 0:
            return True
        else: 
            return False
    
    def pop(self) -> Union[int, None]:
        '''Method that swaps the index at the top to the one at the bottom, deletes the
        old top value, bubbles down the new top index to its appropriate position then 
        returns the removed top value.'''
        if self.is_empty():
            return None
        else:
            self.swap(1, self.last_index())
            popped_item = self.heap.pop()
            self.bubble_down(1)
            return popped_item
        
    def validate(self) -> None:
        for index, value in enumerate(self.heap):
            if index == 0:
                continue
            parent = self.parent(index)
            child_l, child_r = self.children(index)
            if parent is not None:
                not_smaller_than_parent = value > self.heap[parent]
            else:
                not_smaller_than_parent = False

            if child_l is not None:
                not_bigger_than_child_l = value < self.heap[child_l]
            else:
                not_bigger_than_child_l = False

            if child_r is not None:
                not_bigger_than_child_r = value < self.heap[child_r]
            else:
                not_bigger_than_child_r = False

            if not_smaller_than_parent:
                raise ValueError(
                    f"Node of value {value} is not smaller than parent of value {self.heap[parent]}"
                )
            if not_bigger_than_child_l:
                raise ValueError(
                    f"Node of value {value} is not bigger than left child of value {self.heap[child_l]}"
                )
            if not_bigger_than_child_r:
                raise ValueError(
                    f"Node of value {value} is not bigger than right child of value {self.heap[child_r]}"
                )
        print(self)
        print("***** Heap above is Valid! *****")


        
    def __str__(self) -> str:
        # copy our heap
        str_heap = copy(self.heap)
        # remove the 0 element
        del str_heap[0]
        # turn into string, then return it
        str_heap = str(str_heap)
        return str_heap

if __name__ == "__main__":        
    v = MaxHeap(1,5,6,78,8,9,128,892)
    print(v)

