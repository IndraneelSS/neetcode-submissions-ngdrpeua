class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create count arrays for s1 and the current window in s2
        s1Count, window_s2Count = [0] * 26, [0] * 26

        # Populate the counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            window_s2Count[ord(s2[i]) - ord('a')] += 1

        # Start sliding the window across s2
        for i in range(len(s2) - len(s1)):
            if window_s2Count == s1Count:
                return True
            
            # Slide the window: remove the character going out and add the new one
            window_s2Count[ord(s2[i]) - ord('a')] -= 1
            window_s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1

        # Check the final window after the loop
        return window_s2Count == s1Count





 

        