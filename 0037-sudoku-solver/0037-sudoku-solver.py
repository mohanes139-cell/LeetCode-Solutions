class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        # Initialize bitmasks with already placed numbers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    mask = 1 << int(val)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask
                else:
                    empty_cells.append((r, c))

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            # Mask representing numbers 1-9 already used in row, col, or box
            used = rows[r] | cols[c] | boxes[box_idx]

            for d in range(1, 10):
                mask = 1 << d
                if not (used & mask):
                    # Place digit
                    board[r][c] = str(d)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

                    if backtrack(index + 1):
                        return True

                    # Undo placement (backtrack)
                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[box_idx] &= ~mask

            return False

        backtrack(0)