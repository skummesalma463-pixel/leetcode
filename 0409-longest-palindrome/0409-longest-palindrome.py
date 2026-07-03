class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        ans=0
        odd=False
        for v in d.values():
            if v%2==0:
                ans+=v
            else:
                ans+=v-1
                odd=True
        if odd:
            ans+=1
        return ans
        