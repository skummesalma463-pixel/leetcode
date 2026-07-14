
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans=-1
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]-nums[i]!=1:
                continue
            l=2
            s=1
            for j in range(i+1,n-1):
                if nums[j+1]-nums[j]==-s:
                    l+=1
                    s*=-1
                else:
                    break
            ans=max(ans,l)
        return ans
