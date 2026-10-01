from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
        
        word_count = Counter(words)
        result = []
        
        # Check each possible word-alignment offset
        for offset in range(word_len):
            left = offset
            right = offset
            current_count = Counter()
            words_used = 0
            
            # Slide the window by word chunks
            while right + word_len <= s_len:
                sub = s[right:right + word_len]
                right += word_len
                
                if sub in word_count:
                    current_count[sub] += 1
                    words_used += 1
                    
                    # If there are more occurrences than allowed, shrink from the left
                    while current_count[sub] > word_count[sub]:
                        left_sub = s[left:left + word_len]
                        current_count[left_sub] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # If all words matched with exact counts
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Reset if word not in list
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return result