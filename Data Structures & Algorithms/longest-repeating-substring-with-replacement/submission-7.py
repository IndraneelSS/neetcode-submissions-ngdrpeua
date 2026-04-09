class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_frequency = {}
        result = 0
        start = 0
        end = 0
        max_frequency = 0

        for end in range(len(s)):
            count_frequency[s[end]] = 1 + count_frequency.get(s[end],0)
            max_frequency = max(max_frequency,count_frequency[s[end]])

            while (end-start+1) - max_frequency > k:
                count_frequency[s[start]] -= 1
                start += 1

            result  = max(result,end-start+1)  

        return result      




        