# This code can be solved using 2 methods 
# one is transpose  and then reverse each row 
# second used by neet code solution 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
        