class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_capacity = 0

        while i < j:
            length = j - i
            height = min(heights[i], heights[j])
            area_capacity = length * height
            max_capacity = max(max_capacity, area_capacity)

            # Move the pointer with the smaller height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1  

        return max_capacity

             



        