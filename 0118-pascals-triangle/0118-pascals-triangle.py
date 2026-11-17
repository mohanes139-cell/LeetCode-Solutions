class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for _ in range(numRows - 1):
            res.append(list(map(sum, zip([0] + res[-1], res[-1] + [0]))))
        return res