class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
    

#Sets have an average time complexity of O(1) 
#for operations like add(), remove(), and checking membership (in).

#Sets inherently store only unique elements, which aligns perfectly 
#with the problem of finding substrings without duplicates.



        