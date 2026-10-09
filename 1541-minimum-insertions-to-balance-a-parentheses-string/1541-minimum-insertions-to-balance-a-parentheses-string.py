class Solution:
    def minInsertions(self, s: str) -> int:
        res = need = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
                i += 1
            else:
                if need > 0:
                    need -= 1
                else:
                    res += 1
                    need = 1
                i += 1
        return res + need