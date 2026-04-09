from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed and sort by position in descending order
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        fleets = 0
        prev_time = 0  # Tracks when the last fleet arrives at target
        
        for pos, spd in cars:
            # Calculate time needed for current car to reach target
            time = (target - pos) / spd
            
            # If this car arrives later than the fleet ahead, it forms a new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets
        