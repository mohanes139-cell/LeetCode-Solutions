class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = []
            # Iterate through the string in chunks of size k
            for i in range(0, len(s), k):
                group = s[i:i+k]
                # Sum the digits in the current group and convert back to string
                group_sum = sum(int(digit) for digit in group)
                new_s.append(str(group_sum))
            
            # Merge the groups into the updated string for the next round
            s = "".join(new_s)
            
        return s