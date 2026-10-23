from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts = {}
        left = 0
        formed = 0

        # Stores (window_length, left, right)
        ans = (float("inf"), None, None)

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract window from left while it remains valid
            while left <= right and formed == required:
                # Update answer if current window is smaller
                window_len = right - left + 1
                if window_len < ans[0]:
                    ans = (window_len, left, right)

                remove_char = s[left]
                window_counts[remove_char] -= 1
                if remove_char in target_counts and window_counts[remove_char] < target_counts[remove_char]:
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]