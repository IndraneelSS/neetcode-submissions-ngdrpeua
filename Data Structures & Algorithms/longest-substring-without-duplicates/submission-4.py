class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        character_set = set()

        left  = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in character_set:
                character_set.remove(s[left])
                left += 1
            character_set.add(s[right])    
            max_length = max(max_length,right-left+1)
            right += 1

        return max_length    


        