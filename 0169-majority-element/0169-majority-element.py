class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # for i in range(n):
        #     count=0
        #     for j in range(n):
        #         if nums[i]==nums[j]:
        #             count +=1
        #     if count>n//2:
        #         return nums[i]    
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count +=1
            else:
                count -=1
        return candidate