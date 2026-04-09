class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True    



# Set -*Elements only (no key-value pairs).
#      *Automatically removes duplicates.
#      *Unordered, so elements don’t have a specific position.    

# my_set = {1, "apple", 3.14}
#Hash of 1: 1
#Hash of 'apple': -4177319843348743657
#Hash of 3.14: 322818021289917443
# hash values are randomized 

# Hashmap 
# Based on key-value pairs 
# * my_dict = {'name': 'John', 'age': 30}
# * print(my_dict['name'])  # Output: John
# * my_dict['age'] = 31 
        