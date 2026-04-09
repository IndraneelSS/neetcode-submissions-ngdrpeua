#max(frequency_map, key=frequency_map.get)
#min(frequency_map, key=frequency_map.get)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = self.frequency_counter(nums)
        sorted_elements = sorted(frequency_map, key=frequency_map.get, reverse=True)
        return sorted_elements[:k] 

    def frequency_counter(self, nums):
        frequency_list = {}
        for s in nums:
            if s in frequency_list:
                frequency_list[s] += 1
            else:
                frequency_list[s] = 1  # This should be inside `else`
        return frequency_list  



        