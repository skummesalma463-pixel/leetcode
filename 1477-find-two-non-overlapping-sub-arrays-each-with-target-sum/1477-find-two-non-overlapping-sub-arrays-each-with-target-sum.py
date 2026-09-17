class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr);d={0:0};s=0;m=float('inf');ans=float('inf')
        ml=[float('inf')]*n
        for i,v in enumerate(arr):
            s+=v
            if s-target in d:
                l=i-d[s-target]+1
                if d[s-target] > 0 and ml[d[s-target]-1]!=float('inf'):
                    ans=min(ans,l+ml[d[s-target]-1])
                m=min(m,l)
            ml[i]=m
            d[s]=i+1
        return ans if ans!=float('inf') else -1