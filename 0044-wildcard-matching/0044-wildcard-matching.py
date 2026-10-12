class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx = -1
        s_tmp_idx = -1

        s_len, p_len = len(s), len(p)

        while s_idx < s_len:
            # 1. Characters match or pattern has '?'
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            # 2. Pattern has '*', record its position and assume it matches empty string
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            # 3. Mismatch: backtrack to the last '*' and let it match one more character
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_tmp_idx += 1
                s_idx = s_tmp_idx
            # 4. Mismatch with no prior '*'
            else:
                return False

        # Consume any trailing '*' in pattern
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1

        return p_idx == p_len