class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            # Push the expected closing bracket
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            else:
                # Closing bracket must match the top of stack
                if not stack or stack.pop() != ch:
                    return False

        # Stack should be empty if all brackets matched
        return not stack
     


                  

        