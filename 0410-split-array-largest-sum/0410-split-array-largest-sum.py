class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # if k!=2:
        #     return -1
        # ans=float('inf')
        # for i in range(1,n):
        #     left=nums[:i]
        #     right=nums[i:]
        #     cost=max(sum(left),sum(right))
        #     ans=min(ans,cost)
        # return ans
        def canSplit(maxSum):
            count=1
            currentSum=0
            for num in nums:
                if currentSum+num>maxSum:
                    count+=1
                    currentSum=num
                else:
                    currentSum+=num
            return count<=k
        left=max(nums)
        right=sum(nums)
        while left<right:
            mid=(left+right)//2
            if canSplit(mid):
                right=mid
            else:
                left=mid+1
        return left
