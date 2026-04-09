class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        frequency_s  = {}
        frequency_t   = {} 

        for i in s:
            if i in frequency_s:
                frequency_s[i] += 1
            else:
                frequency_s[i] = 1  

        for j in t:
            if j in frequency_t:
                frequency_t[j] += 1
            else:
                frequency_t[j] = 1

        if frequency_s.items() == frequency_t.items():
            return True 

        else:
            return False          




        