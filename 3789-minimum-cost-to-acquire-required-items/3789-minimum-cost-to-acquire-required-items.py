class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        common = min(need1, need2)
        rem1 = need1 - common
        rem2 = need2 - common
        
        total_cost = (
            common * min(costBoth, cost1 + cost2)
            + rem1 * min(cost1, costBoth)
            + rem2 * min(cost2, costBoth)
        )
        
        return total_cost