class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        for i, ch in enumerate(seq):
            if ch == '(':
                res.append(i % 2)
            else:
                res.append(1 - (i % 2))
        return res