from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_of_input = len(nums)

        # Initialize result array with 1s
        output_array = [1] * length_of_input

        # Calculate the prefix product for each element
        prefix_value = 1
        for i in range(length_of_input):
            output_array[i] = prefix_value
            prefix_value *= nums[i]

        # Calculate the postfix product and multiply with the existing result
        postfix_value = 1
        for j in range(length_of_input - 1, -1, -1):
            output_array[j] *= postfix_value
            postfix_value *= nums[j]

        return output_array

                






        