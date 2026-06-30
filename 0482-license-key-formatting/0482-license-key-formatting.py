class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        ans=""
        c=0
        for i in range(len(s)-1,-1,-1):
            if c==k:
                ans="-"+ans
                c=0
            ans=s[i]+ans
            c+=1
        return ans