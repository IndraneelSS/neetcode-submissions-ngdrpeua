class Solution:
    def isPalindrome(self, s: str) -> bool:
               
        cleaned_string = ''.join(filter(str.isalnum, s)).lower()

        left = 0
        right  = len(cleaned_string) - 1

        while left <= right:
            if cleaned_string[left] == cleaned_string[right]:
                left  += 1
                right -= 1

            else:
                return False 
            


        return True     



                     


        