class Solution:
    def isValid(self, s: str) -> bool:
        st = []  # Initialize an empty stack
        for it in s:
            # If the character is an opening bracket, push it onto the stack
            if it == '(' or it == '{' or it == '[':
                st.append(it)
            else:
                # If the stack is empty when a closing bracket is encountered, return False
                if len(st) == 0:
                    return False
                
                # Check if the top of the stack matches the current closing bracket
                if (it == ')' and st[-1] == '(') or (it == ']' and st[-1] == '[') or (it == '}' and st[-1] == '{'):
                    st.pop()  # Pop after confirming the match
                else:
                    return False
        
        # In the end, the stack should be empty if all brackets were matched
        return len(st) == 0

        