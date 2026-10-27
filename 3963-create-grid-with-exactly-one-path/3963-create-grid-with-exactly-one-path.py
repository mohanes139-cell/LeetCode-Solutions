class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        
        # First row: move all the way to the right
        grid.append("." * n)
        
        # Remaining rows: go down along the last column, blocking everything else
        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")
            
        return grid