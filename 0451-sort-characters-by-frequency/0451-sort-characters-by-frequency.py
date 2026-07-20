from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        return "".join(ch*f for ch,f in sorted(c.items(),key=lambda x:-x[1]))