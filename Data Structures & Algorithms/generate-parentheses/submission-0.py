
# pop() reverts the stack to try other paths
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n: #this is the base case
                res.append("".join(stack))
            
                return

            if openN < n:
                stack.append("(")  
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res                              
        
        