from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    # Step 1: Count frequency of each factor (constraints: 1 <= factor <= 1500)
    max_factor = max(f for f, _ in items)
    freq = [0] * (max_factor + 1)
    for f, _ in items:
      freq[f] += 1

    # Step 2: Precompute total copies gained from buying the FIRST copy of factor f
    # This includes the purchased item itself (1) + all other items j != i divisible by f
    gain_by_factor = [0] * (max_factor + 1)
    for f in range(1, max_factor + 1):
      if freq[f] > 0:
        multiples_count = 0
        for multiple in range(f, max_factor + 1, f):
          multiples_count += freq[multiple]
        # multiples_count includes item i itself, so total copies = multiples_count
        gain_by_factor[f] = multiples_count

    # Step 3: 0/1 Knapsack for activating (buying first copy of) items
    # Use -1 to mark unreachable exact budgets
    dp = [-1] * (budget + 1)
    dp[0] = 0
    min_price = float('inf')

    for f, p in items:
      min_price = min(min_price, p)
      g = gain_by_factor[f]
      for c in range(budget, p - 1, -1):
        if dp[c - p] != -1:
          dp[c] = max(dp[c], dp[c - p] + g)

    # Step 4: Fill any leftover budget with the cheapest item available
    ans = 0
    for c in range(budget + 1):
      if dp[c] != -1:
        extra_copies = (budget - c) // min_price
        ans = max(ans, dp[c] + extra_copies)

    return ans