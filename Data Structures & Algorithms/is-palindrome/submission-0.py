class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()        # Remove all non-alphanumeric characters using regex
        cleaned_string = re.sub(r'[^a-z0-9]', '', s)
        left = 0
        right = len(cleaned_string)-1
        


        while left<=right:
            if cleaned_string[left]==cleaned_string[right]:
                left +=1
                right -=1
            else: 
                return False 
        return True             




        