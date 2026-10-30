class Solution:

  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)

    if m + n != len(s3):
      return False

    # dp[j] will store whether s1[0:i] and s2[0:j] can interleave to form s3[0:i+j]
    dp = [False] * (n + 1)
    dp[0] = True

    # Base row: using only s2 to match s3 prefix
    for j in range(1, n + 1):
      dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    # Process each character of s1
    for i in range(1, m + 1):
      # First column: using only s1
      dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

      for j in range(1, n + 1):
        char_s3 = s3[i + j - 1]

        # Valid either by taking s1[i-1] (coming from previous row dp[j])
        # or taking s2[j-1] (coming from current row left neighbor dp[j-1])
        take_s1 = dp[j] and s1[i - 1] == char_s3
        take_s2 = dp[j - 1] and s2[j - 1] == char_s3

        dp[j] = take_s1 or take_s2

    return dp[n]