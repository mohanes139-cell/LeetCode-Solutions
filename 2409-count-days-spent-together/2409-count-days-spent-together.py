class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date: str) -> int:
            month, day = map(int, date.split('-'))
            return sum(days_per_month[:month - 1]) + day
        
        start_a, end_a = to_day_of_year(arriveAlice), to_day_of_year(leaveAlice)
        start_b, end_b = to_day_of_year(arriveBob), to_day_of_year(leaveBob)
        
        # Overlapping interval starts at the later arrival and ends at the earlier departure
        overlap_start = max(start_a, start_b)
        overlap_end = min(end_a, end_b)
        
        return max(0, overlap_end - overlap_start + 1)