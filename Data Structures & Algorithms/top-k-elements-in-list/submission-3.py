class Solution:
    def count_frequency(self, nums):
        frequency_list = {}
        for element in nums:
            if element in frequency_list:
                frequency_list[element] += 1
            else:
                frequency_list[element] = 1  
        return frequency_list

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map = self.count_frequency(nums)  # Get frequency of elements
        # Sort elements by frequency in descending order and pick the top k
        sorted_elements = sorted(frequency_map, key=frequency_map.get, reverse=True)
        
        # Return the top k most frequent elements
        return sorted_elements[:k]       
                

        
        


        
        