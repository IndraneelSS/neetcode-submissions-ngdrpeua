class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        frequency ={}

        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        for i,count in frequency.items():
            if count == 1:
                return i       

        