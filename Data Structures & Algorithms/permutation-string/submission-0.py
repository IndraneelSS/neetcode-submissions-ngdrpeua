from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the length of s1 and s2
        len_s1, len_s2 = len(s1), len(s2)

        # If s1 is longer than s2, return False immediately
        if len_s1 > len_s2:
            return False

        # Create a counter for s1 and for the first window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])

        # Slide the window over s2
        for i in range(len_s2 - len_s1):
            # If the current window matches s1's count, return True
            if s1_count == window_count:
                return True

            # Slide the window: remove the character going out of the window and add the new character
            window_count[s2[i]] -= 1
            if window_count[s2[i]] == 0:
                del window_count[s2[i]]  # Remove the character from the count if it goes to 0

            window_count[s2[i + len_s1]] += 1  # Add the new character to the window

        # Check the last window
        return s1_count == window_count

        