class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        
        # Length 2 and not sorted cannot be fixed
        if n == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # Case 1: An anchor is already at an endpoint
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # Case 2: An extremum exists in the interior
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        
        # Case 3: s[0] == mx and s[-1] == mn with neither in between
        return 3