class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Set to track previously seen numbers
        
        while n != 1:
            digits = []
            
            # Extract digits of the current number
            while n > 0:
                digits.append(n % 10)  # Extract the last digit
                n = n // 10  # Remove the last digit from the number
            
            # Calculate the sum of squares of digits
            sum_ = 0
            for digit in digits:
                sum_ += digit * digit
            
            # If the sum is 1, it's a happy number
            if sum_ == 1:
                return True
            
            # If the number has been seen before, it's a loop, and hence not happy
            if sum_ in seen:
                return False
            
            # Add the current sum to the set of seen numbers
            seen.add(sum_)
            
            # Set n to the sum of squares for the next iteration
            n = sum_
        
        return True  # If n becomes 1, it's a happy number



            

            


    
    
        