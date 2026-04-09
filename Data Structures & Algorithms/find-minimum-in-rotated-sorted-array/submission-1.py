class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_value = 1001


        while left <= right:
            if nums[left] > nums[right]:
                left = left + 1
            else:

                mid = (left + right)//2
                min_value = min(min_value,nums[mid])
                right  = mid - 1 

        return min_value         



        