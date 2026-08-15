class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if any(x != 0 for x in nums):
            if len(set(nums)) == 1 and 0 in nums:
                return len(nums) - 1
            total = 0
            for x in nums:
                total ^= x
            if total != 0:
                return len(nums)
            else:
                return len(nums) - 1
        return 0