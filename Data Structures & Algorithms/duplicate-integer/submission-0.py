class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_list = {}
        for element in nums:
            if element in frequency_list:
                return True
            else:
                frequency_list[element] = 1  

        return False
         