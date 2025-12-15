class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        prefix = strs[0]

        for word in strs:
            while prefix not in word[:len(prefix)]:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
