class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        add_count = 0
        
        for ch in s:
            if ch == '(':
                open_needed += 1
            else:
                if open_needed > 0:
                    open_needed -= 1
                else:
                    add_count += 1
                    
        return add_count + open_needed