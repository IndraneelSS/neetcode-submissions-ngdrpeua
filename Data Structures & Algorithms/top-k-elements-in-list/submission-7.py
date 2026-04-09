from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the top K frequent elements in a list using bucket sort.
        
        Args:
            nums: List of integers.
            k: Number of most frequent elements to return.
            
        Returns:
            List of the top K frequent elements.
        """
        # Step 1: Count frequencies of each element
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # Step 2: Create frequency buckets (index = frequency)
        max_freq = max(freq_map.values())
        buckets = []
        for i in range(max_freq + 1):
            buckets.append([])
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Step 3: Extract top K elements from buckets
        res = []
        for freq in range(max_freq, 0, -1):  # Start from highest frequency
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res[:k]  # Handle edge case (if K > unique elements) 