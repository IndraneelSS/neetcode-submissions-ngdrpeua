#In Python, append() is the correct term for adding an element to a list or stack-like structure.
# push() is more of a conceptual or traditional term used when referring to stack operations,
# but Python does not have a specific push() method.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {'+', '-', '*','/'} :
                stack.append(int(token))

            else:

                 num2 = stack.pop()  # The second operand
                 num1 = stack.pop()   # first 

                 if token == '+':
                    result = num1 + num2

                 elif token == '*':
                    result = num1 * num2 

                 elif token == '-':
                    result = num1 - num2    

                 elif token == '/':
                    result = int(num1/num2)

                 stack.append(result)     
        return stack.pop()          











        