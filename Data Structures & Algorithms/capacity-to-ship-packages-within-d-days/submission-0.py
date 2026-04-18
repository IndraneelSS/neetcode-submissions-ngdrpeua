class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            cap   = (l + r) // 2
            ships = 1
            load  = 0

            for w in weights:
                load += w
                if load > cap:               # package doesn't fit → new day
                    ships += 1
                    load = w                 # start fresh with this package

            if ships <= days:                # integer comparison
                r = cap
            else:
                l = cap + 1

        return l




