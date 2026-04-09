class Solution:
    def longestPalindrome(self, s: str) -> str:

        output = ""
        output_len = 0

        for i in range(len(s)):
            # for odd length
            l, r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > output_len:
                    output_len = r - l + 1
                    output = s[l:r+1]

                l -= 1
                r += 1


            l, r  = i , 1 + i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > output_len:
                    
                    output_len = r - l + 1
                    output = s[l:r+1]

                l -= 1
                r += 1

        return output        



                     
                    




        
        