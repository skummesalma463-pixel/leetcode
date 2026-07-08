class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        r=[]
        for i in nums1:
            d[i]=d.get(i,0)+1
        for i in nums2:
            if d.get(i,0)>0:
                r.append(i)
                d[i]-=1
        return r