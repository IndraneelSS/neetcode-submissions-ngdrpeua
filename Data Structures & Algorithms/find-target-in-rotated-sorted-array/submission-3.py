class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:  # Use <= to include both l and r
            mid = l + (r - l) // 2

            if nums[mid] == target:  # Target found
                return mid

            # Left part is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Focus on the left half
                else:
                    l = mid + 1  # Focus on the right half

            # Right part is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Focus on the right half
                else:
                    r = mid - 1  # Focus on the left half

        return -1  # Target not found
             

        