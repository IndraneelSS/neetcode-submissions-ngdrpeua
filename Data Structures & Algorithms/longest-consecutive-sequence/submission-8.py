class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        number_set = set(nums)
        longest = 0

        for num in number_set:
            if (num-1) not in number_set:
                length = 1
                while (num+length) in number_set:
                    length += 1
                longest = max(length,longest)
        return longest          


        