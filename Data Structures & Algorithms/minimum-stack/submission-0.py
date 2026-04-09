class MinStack:

    def __init__(self):
        self.minStack = []          # Main stack to store all values
        self.minValueStack = []     # Auxiliary stack to keep track of minimum values

    def push(self, val: int) -> None:
        self.minStack.append(val)
        # Update the minimum value stack
        if not self.minValueStack:  # If minValueStack is empty
            self.minValueStack.append(val)
        else:
            current_min = self.minValueStack[-1]
            self.minValueStack.append(min(val, current_min))

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()    
            self.minValueStack.pop()  # Pop from the minValueStack as well

    def top(self) -> int:
        return self.minStack[-1] if self.minStack else None  # Return None if the stack is empty

    def getMin(self) -> int:
        return self.minValueStack[-1] if self.minValueStack else None  # Return None if minValueStack is empty



        
