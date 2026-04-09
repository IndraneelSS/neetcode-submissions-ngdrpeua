class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Check for empty input
        if not strs:
            return []

        # Dictionary to store groups of anagrams
        frequency_strings_map = defaultdict(list)

        for s in strs:
            # Get the frequency string representation
            frequency_string = self.get_frequency_string(s)
            # Add the string to the corresponding frequency key
            frequency_strings_map[frequency_string].append(s)

        # Return the grouped anagrams as a list of lists
        return list(frequency_strings_map.values())

    def get_frequency_string(self, s: str) -> str:
        # Array to store character frequency for 'a' to 'z'
        freq = [0] * 26  

        # Count the frequency of each character
        for char in s:
            freq[ord(char) - ord('a')] += 1  

        # Create a unique frequency string
        frequency_string = []
        for i in range(26):
            frequency_string.append(chr(ord('a') + i))  # Append character
            frequency_string.append(str(freq[i]))  # Append frequency count

        return "".join(frequency_string)


        