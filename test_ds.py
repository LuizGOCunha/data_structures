from maxheap_class import MaxHeap
from random import randint
import pytest

def rn(range:int) -> int:
    '''Returns random number everytime its called'''
    return randint(0, range)

class TestDataStructures:

    def test_maxheap(self):
        for n in range(1,200):
            heap = []
            for _ in range(n):
                heap.append(rn(100))
                maxheap = MaxHeap(*heap)
                maxheap.validate()


        

