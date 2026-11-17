class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
        # 1. Precompute proper divisors for every length from 2 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # Helper to calculate min changes to make s[i..j] a semi-palindrome
        def get_cost(i, j):
            length = j - i + 1
            min_changes = float('inf')
            
            for d in divisors[length]:
                changes = 0
                group_len = length // d
                # Check each of the d interleaved groups
                for offset in range(d):
                    left = i + offset
                    right = i + offset + (group_len - 1) * d
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
                    
            return min_changes

        # 2. Precompute cost[i][j] for all valid substrings (length >= 2)
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)
                
        # 3. DP to partition s[0..j-1] into p semi-palindromes
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # Each part requires at least 2 characters
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] != float('inf'):
                        dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i][j - 1])
                        
        return dp[k][n]
        