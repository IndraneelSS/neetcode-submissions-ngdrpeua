# always remember , we always play with the rows and columns in Graph qquestions 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        def addcell(r,c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1 or
            (r,c) in visited):
                return 
            q.append([r,c])  
            visited.add((r,c))  

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))


        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft() 
                grid[r][c] = dist
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)

            dist+= 1    








        