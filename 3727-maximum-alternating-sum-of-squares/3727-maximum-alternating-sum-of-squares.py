class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = sorted(x * x for x in nums)

        ans = 0
        mid = len(nums) // 2

        for i in range(len(nums)):
            if i < mid:
                ans -= nums[i]
            else:
                ans += nums[i]

        return ans