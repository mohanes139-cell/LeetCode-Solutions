from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        # Pruning 1: Board must have at least as many characters as word requires
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        
        # Pruning 2: If the suffix character is rarer than the prefix character,
        # search the reversed word to prune dead paths much earlier
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[idx]:
                return False
            
            # Mark cell as visited in-place
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 orthogonal directions
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )
            
            # Backtrack
            board[r][c] = temp
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False