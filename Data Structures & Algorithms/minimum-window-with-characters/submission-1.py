#s_frequency.keys <= t_frequency.keys: This does not work 
# dictionaries does not support direct Key comparison 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Build frequency map for string t
        t_frequency = {}
        for i in t:  # Iterate over characters in t
            if i in t_frequency:
                t_frequency[i] += 1  # Increment the frequency if the character already exists
            else:
                t_frequency[i] = 1   # Initialize the frequency to 1 if the character is seen

        left = 0
        right = 0
        s_frequency = {}
        
        # To track the minimum window
        min_len = float('inf')  # Start with an infinitely large length
        min_window = ""         # Store the result window substring
        
        # Helper function to check if the current window satisfies the condition
        def contains_all_chars():
            for char, count in t_frequency.items():
                if char in s_frequency:
                    if s_frequency[char] < count:
                        return False  # If the frequency in s_frequency is less than required
                else:
                    return False  # If the character is not in s_frequency at all (treated as frequency 0)
            return True


        # Sliding window logic
        while right < len(s):
            # Add the current character in s to s_frequency
            if s[right] in s_frequency:
                s_frequency[s[right]] += 1
            else:
                s_frequency[s[right]] = 1 

            # Try to shrink the window when it contains all characters
            while contains_all_chars():
                # Update the minimum window if the current one is smaller
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right+1]

                # Shrink the window from the left
                if s[left] in s_frequency:
                    s_frequency[s[left]] -= 1
                    if s_frequency[s[left]] == 0:
                        del s_frequency[s[left]]  # Remove character from frequency if it's no longer in the window
                left += 1  # Move the left pointer to shrink the window

            # Move the right pointer to expand the window
            right += 1

        # Return the minimum window substring found
        return min_window








        