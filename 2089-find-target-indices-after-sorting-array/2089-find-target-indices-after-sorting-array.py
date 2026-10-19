class Solution:
    def targetIndices(self,nums:list[int],target:int)->list[int]:
        s=sorted(nums)
        return[i for i,x in enumerate(s)if x==target]