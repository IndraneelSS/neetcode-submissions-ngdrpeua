from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        # Convert the list of digits to a single number
        for i in digits:
            number = number * 10 + i

        # Add 1 to the number
        number += 1

        # Convert the number back into a list of digits and return
        return [int(digit) for digit in str(number)]
  
        