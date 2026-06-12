class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={0:1}
        s=0
        c=0
        for n in nums:
            s+=n
            if s-goal in d:
                c+=d[s-goal]
            d[s]=d.get(s,0)+1
        return c