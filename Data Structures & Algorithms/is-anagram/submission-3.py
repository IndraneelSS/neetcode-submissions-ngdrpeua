class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_list_s = {}
        for element in s:
            if element in frequency_list_s:
                frequency_list_s[element] += 1
            else:
                frequency_list_s[element] = 1  
        

        frequency_list_t = {}
        for element in t:
            if element in frequency_list_t:
                frequency_list_t[element] += 1
            else:
                frequency_list_t[element] = 1 


        if frequency_list_s.items() == frequency_list_t.items():
            return True 
        else:
            return False    


# Even this is solved using Hashing_count_frequency concept                     
#array.values(): Returns a view of all values.
#array.keys(): Returns a view of all keys.
#array.get(key, default_value): Safely retrieves a value by key, with an optional default if the key doesn’t exist.
#array.items(): Returns a view of all key-value pairs as tuples.    
        