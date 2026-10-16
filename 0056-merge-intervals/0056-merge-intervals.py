class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged is empty or current interval does not overlap with the previous
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlap detected; extend the previous interval's end
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged