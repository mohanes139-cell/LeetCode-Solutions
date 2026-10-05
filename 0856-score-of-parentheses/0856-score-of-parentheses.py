class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        bal = 0
        
        for i, char in enumerate(s):
            if char == '(':
                bal += 1
            else:
                bal -= 1
                # If we encounter a base core "()", add 2^bal to the score
                if s[i - 1] == '(':
                    ans += 1 << bal
                    
        return ans