class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # for ex - values = [("morning", 1), ("afternoon", 2), ("night", 5)]
            # I want to access the timestap 1 then as l =0, r = 2 (value-0,1,2)
            # mid = 2//2 = 1  then mid will point to 2 ie values[1][1] = 2 , but not equal to target timestamp
            # so right moves forward than mid and recalculates, we get mid = 0 then values[0][1] = 1 == target timestamp
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
           
         







        
