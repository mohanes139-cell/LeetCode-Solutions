class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        # If nums is already sorted, every divisor k is automatically valid
        if nums == s:
            divisors_sum = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors_sum += i
                    if i * i != n:
                        divisors_sum += n // i
            return divisors_sum

        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_k_sum = 0
        
        for k in divisors:
            possible = True
            
            for start in range(0, n, k):
                # Count drops where block[i] > block[i + 1] cyclically
                drops = 0
                drop_idx = -1
                
                # Check adjacent pairs within the block
                for i in range(start, start + k - 1):
                    if nums[i] > nums[i + 1]:
                        drops += 1
                        drop_idx = i - start
                        if drops > 1:
                            break
                            
                # Check wraparound from end of block to start
                if drops <= 1 and nums[start + k - 1] > nums[start]:
                    drops += 1
                    if drops == 1:
                        drop_idx = k - 1
                
                if drops > 1:
                    possible = False
                    break
                
                # If drops == 0, all elements in the block are non-decreasing cyclically (e.g., identical or already sorted)
                # If drops == 1, the rotation offset where it should start is (drop_idx + 1) % k
                rot = 0 if drops == 0 else (drop_idx + 1) % k
                
                # Verify that rotating by `rot` matches the target slice in s
                # Comparing element by element avoids extra list allocations
                for j in range(k):
                    if nums[start + (rot + j) % k] != s[start + j]:
                        possible = False
                        break
                
                if not possible:
                    break
                    
            if possible:
                total_k_sum += k
                
        return total_k_sum