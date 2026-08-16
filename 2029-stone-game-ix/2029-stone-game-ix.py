class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0, 0, 0]
        for s in stones:
            c[s % 3] += 1
        if c[1] == 0 and c[2] == 0:
            return False
        if c[1] == 0 or c[2] == 0:
            return c[0] % 2 != 0 and abs(c[1] - c[2]) > 2
        if c[0] % 2 == 0:
            return True
        return abs(c[1] - c[2]) > 2