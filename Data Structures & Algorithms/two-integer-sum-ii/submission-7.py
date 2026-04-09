class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if target == sum_:
                return [left+1,right+1]

            elif target < sum_:
                right -= 1

            else:
                left += 1
                        
        