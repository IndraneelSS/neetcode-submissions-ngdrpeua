import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create minheap with K largest integers
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)  # Convert array into min-heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Fixed: use self.minHeap
        if len(self.minHeap) > self.k:     # Fixed: use self.k
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  
        

        
