
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        frequency_list = {}

        for num in nums:  # num takes on the value of each element in nums
            if num in frequency_list:  # Check if this value has already been seen
                return num  # Return the duplicate number
            else:
                frequency_list[num] = 1  # Mark this number as seen

          # If no duplicate found





        