class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Ensure word2 is the shorter string for O(min(m, n)) space
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m

        # dp[j] stores edit distance from word1 prefix to word2[:j]
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] = i  # word1[:i] to empty string requires i deletions

            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = 1 + min(
                        dp[j],  # deletion from word1
                        dp[j - 1],  # insertion into word1
                        prev_diag,  # replacement
                    )
                prev_diag = temp

        return dp[n]