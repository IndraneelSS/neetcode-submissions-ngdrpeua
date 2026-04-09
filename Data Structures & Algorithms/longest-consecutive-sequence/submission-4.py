
# you need to check the three conditions - 
# if the current element is 1 value greater tha the prev_curr, then increase the
# counter.
# if not then 2 possibilities  -  one different value or duplicate value
# if diff value then reset the countwer , if duplicate skip it not count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue  # skip duplicates
            elif nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1  # reset
        
        # Final comparison in case the longest sequence is at the end
        longest_streak = max(longest_streak, current_streak)
        
        return longest_streak           


       

        