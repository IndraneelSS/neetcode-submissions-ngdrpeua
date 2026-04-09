class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)  # Initialize with zeros
    
        for i in range(len(temperatures)-1, -1, -1):  # Fix range
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
        
            if stack:
                output[i] = stack[-1] - i
            stack.append(i)
    
        return output






        