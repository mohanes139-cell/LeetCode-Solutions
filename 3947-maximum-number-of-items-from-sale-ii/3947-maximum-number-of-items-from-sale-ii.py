from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # 1. Count frequencies of each factor (1 <= factor <= n)
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # 2. Compute multiples_count[f] = total items whose factor is divisible by f
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for m in range(f, n + 1, f):
                    multiples_count[f] += freq[m]
                    
        # 3. Sort items by price ascending
        items.sort(key=lambda x: x[1])
        
        min_price = items[0][1]
        total_items = 0
        
        # 4. Buy value-2 boosted copies while cheaper than buying two min_price items
        for factor, price in items:
            if price >= 2 * min_price or budget < price:
                break
                
            gain = multiples_count[factor] - 1  # Exclude self (i != j)
            if gain > 0:
                take = min(gain, budget // price)
                total_items += 2 * take
                budget -= take * price
                
        # 5. Spend any remaining budget on the single cheapest item (value-1 each)
        total_items += budget // min_price
        
        return total_items