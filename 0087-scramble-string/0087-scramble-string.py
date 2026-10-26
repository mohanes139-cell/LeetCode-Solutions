from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # Prune branches where character counts do not match
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: No swap
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            
            # Case 2: Swapped
            if self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i]):
                return True
                
        return False