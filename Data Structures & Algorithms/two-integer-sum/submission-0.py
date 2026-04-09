class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        

# Hashmap catch hold of all the elements , until it the 
# iterator, but the pointer approach - just holds the 
# element  that is currently present value , so that is 
# reason why only in one run , we can get the answer

# Whenever your working with hash map, you must intializa 
# idex variable and Num 