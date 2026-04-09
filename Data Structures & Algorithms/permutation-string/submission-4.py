from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if a permutation of s1 exists as a substring in s2.
        
        Args:
            s1: The string whose permutations we're checking for
            s2: The string to search within
            
        Returns:
            bool: True if a permutation exists, False otherwise
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = defaultdict(int)
        window_count = defaultdict(int)
        
        # Initialize frequency counts
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            window_count[s2[i]] += 1
        
        if s1_count == window_count:
            return True
        
        # Slide the window through s2
        for i in range(len(s1), len(s2)):
            # Add new character to the right of window
            window_count[s2[i]] += 1
            
            # Remove character leaving the left of window
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Compare counts
            if s1_count == window_count:
                return True
        
        return False
        