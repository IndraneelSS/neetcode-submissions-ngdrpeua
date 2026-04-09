class Solution:
    def solve(self, board: List[List[str]]) -> None:

        directions_for_each_cell = [[0,1],[1,0],[-1,0],[0,-1]]
        row_movement = len(board)
        column_movement = len(board[0])

        def capture(r,c):
            if (r<0 or c<0 or r==row_movement or c==column_movement
                or board[r][c] != "O"):

                return 
            # which means there is O inside the graph , 
            # here we need to start to implement the DFS algo
            # for the neighbourhood cells 

            board[r][c] = "T"
            for dr, dc in directions_for_each_cell:
                capture(r + dr, c + dc)

        for r in range(row_movement):
            if board[r][0] == "O": # first border row 
                capture(r,0)
            if board[r][column_movement - 1] =="O": # last border row 
                capture(r,column_movement - 1)    

        for c in range(column_movement):
            if board[0][c] == "O":
                capture(0,c)  
            if board[row_movement -1 ][c] == "O":
                capture(row_movement -1, c)

        for r in range(row_movement):
            for c in range(column_movement):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"


        