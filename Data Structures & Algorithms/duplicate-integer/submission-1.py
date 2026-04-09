class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_list = {}

        # Count occurrences of each number
        for i in nums:
            if i in frequency_list:
                frequency_list[i] += 1
            else:
                frequency_list[i] = 1

        # Check if any element appears more than once
        for count in frequency_list.values():
            if count > 1:
                return True  # Duplicate found

        return False  # No duplicates found







         