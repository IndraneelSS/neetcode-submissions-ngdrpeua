class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        q = deque()

        fresh = 0 

        time = 0 


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh = fresh + 1
                
                elif grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r , c = q.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc 
                    if (0 <= nr < len(grid) and  0 <= nc < len(grid[0]) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh = fresh - 1
                        q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1