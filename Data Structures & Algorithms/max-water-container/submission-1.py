class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_h = 0  # Start left pointer at the beginning
        right_h = len(heights) - 1  # Start right pointer at the end
        max_area = 0  # Initialize max area

        while left_h < right_h:  # Loop until the two pointers meet
            # Calculate the area based on the shorter height and the distance between pointers
            length_of_container = min(heights[left_h], heights[right_h])
            base_of_container = right_h - left_h
            area = length_of_container * base_of_container

            # Update max_area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter height
            if heights[left_h] < heights[right_h]:
                left_h += 1
            else:
                right_h -= 1  # Move the right pointer inward
        
        return max_area  # Return the largest area found      


            


        