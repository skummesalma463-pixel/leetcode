class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        while n>=5:
            Q=n//5
            c +=Q
            n=n//5
        return c
    