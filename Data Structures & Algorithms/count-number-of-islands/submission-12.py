class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        movement_for_each_cell = [[1,0],[0,-1],[-1,0],[0,1]]
        row_grid_size = len(grid)
        column_grid_size = len(grid[0])
        islands = 0

        def dfs(each_row,each_col):  
            if (each_row < 0 or each_row >= row_grid_size or 
                each_col < 0 or each_col >= column_grid_size or 
                grid[each_row][each_col] == '0'):
                return 
        
            grid[each_row][each_col] = "0"
            for directed_row , directed_col in movement_for_each_cell:
                dfs(each_row + directed_row, each_col + directed_col)


        for each_row in range(row_grid_size):
            for each_col in range(column_grid_size):
                if grid[each_row][each_col] == '1':
                    dfs(each_row, each_col)
                    islands += 1


        return islands