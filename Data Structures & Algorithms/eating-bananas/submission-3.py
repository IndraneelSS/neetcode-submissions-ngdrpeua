class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r  = max(piles)
        ans = r  # starting with the worst case scenario 

        while l <= r:
            mid  = (l + r)//2 
            total_hours = 0
            for each_pile in piles:
                total_hours += (each_pile + mid - 1)//mid

            if total_hours <= h:
                ans = mid
                r = mid - 1

            else:
                l = mid+1    
        return ans




        