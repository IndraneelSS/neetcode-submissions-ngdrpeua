from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)  # Use 'nums' instead of 'a'
        if n == 0:
            return 0

        longest = 1
        st = set()
        
        # Step 1: Put all the array elements into a set
        for i in range(n):
            st.add(nums[i])  # Change 'a[i]' to 'nums[i]'

        # Step 2: Find the longest sequence
        for it in st:
            # Step 3: Check if 'it' is a starting number
            if it - 1 not in st:
                # Step 4: Find consecutive numbers
                cnt = 1
                x = it
                
                # Step 5: Count the length of the consecutive sequence
                while x + 1 in st:
                    x += 1
                    cnt += 1
                
                # Step 6: Update the longest length found
                longest = max(longest, cnt)
        
        return longest






  








        