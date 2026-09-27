from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if target == "0000":
            return 0

        # visit initially contains all DEADENDS
        visit = set(deadends)

        # If starting point itself is blocked
        if "0000" in visit:
            return -1

        # Start BFS from "0000"
        q = deque(["0000"])

        # Remember that we have already visited "0000"
        visit.add("0000")

        steps = 0

        while q:
            steps += 1

            for _ in range(len(q)):
                lock = q.popleft()

                # Try all 4 wheels
                for i in range(4):

                    # Turn wheel forward (+1) and backward (-1)
                    for j in [1, -1]:

                        digit = str((int(lock[i]) + j + 10) % 10)

                        # Create the new lock
                        lock_list = list(lock)
                        lock_list[i] = digit
                        nextLock = "".join(lock_list)

                        # Deadend OR already visited?
                        # Skip it.
                        if nextLock in visit:
                            continue

                        # Did we reach the target?
                        if nextLock == target:
                            return steps

                        # Explore this lock later
                        q.append(nextLock)

                        # Remember that we have seen it
                        visit.add(nextLock)

        return -1





        