from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                return True  # duplicate found
        return False  # all elements are unique
       

                


         