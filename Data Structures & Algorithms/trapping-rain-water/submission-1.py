class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # Handle edge case of empty height array
            return 0

        max_l = 0  # Track the maximum height on the left side
        max_r = 0  # Track the maximum height on the right side
        l = 0      # Left pointer starting from the first index
        r = len(height) - 1  # Right pointer starting from the last index
        result = 0  # Initialize result to store the total trapped water

        while l <= r:
            if height[l] <= height[r]:
                # If left side is smaller or equal, process the left pointer
                if height[l] >= max_l:
                    # Update the max height on the left side
                    max_l = height[l]
                else:
                    # Calculate trapped water at position `l`
                    result += max_l - height[l]
                l += 1  # Move the left pointer to the right
            else:
                # If right side is smaller, process the right pointer
                if height[r] >= max_r:
                    # Update the max height on the right side
                    max_r = height[r]
                else:
                    # Calculate trapped water at position `r`
                    result += max_r - height[r]
                r -= 1  # Move the right pointer to the left

        return result  # Return the total amount of trapped water


        