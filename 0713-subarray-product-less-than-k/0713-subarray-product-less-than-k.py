class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        p=1
        l=c=0
        for r in range(len(nums)):
            p *=nums[r]
            while p >=k:
                p //=nums[l]
                l +=1
            c +=(r-l+1)
        return c