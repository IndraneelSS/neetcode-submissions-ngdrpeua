class MinStack:
    def __init__(self):
        self.stack = []  # Stores tuples of (value, min_so_far)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]  # Previous min
            new_min = min(val, current_min)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]  # Return value only
        return -1  # Or raise an error

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]  # Return min_so_far
        return -1  # Or raise an error
        
