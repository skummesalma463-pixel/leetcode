class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        p = {}
        w = {}

        for i in range(len(pattern)):
            if pattern[i] in p and p[pattern[i]] != words[i]:
                return False

            if words[i] in w and w[words[i]] != pattern[i]:
                return False

            p[pattern[i]] = words[i]
            w[words[i]] = pattern[i]

        return True