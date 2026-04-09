# My approach is the best solution. 
# better than neet code 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        n  = len(matrix[0])
        m = len(matrix)
        right  = m*n - 1


        while left <= right:
            mid = left + (right - left)//2 
            updated_row_m = (mid//n)
            updated_column_n = (mid%n)
            mid_value = matrix[updated_row_m][updated_column_n]

            if  mid_value == target:
                return True

            elif mid_value > target:
                right = mid - 1 

            else:
                left =  mid + 1       

        return False         

        