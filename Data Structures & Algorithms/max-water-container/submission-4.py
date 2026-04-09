class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        max_area = 0

        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            max_area = max(max_area,area)

            
            if heights[l] < heights[r]:
               
               l = l + 1 
            else:
                r = r - 1   

        return max_area       


      

            

        
            












            
            

            



        
        