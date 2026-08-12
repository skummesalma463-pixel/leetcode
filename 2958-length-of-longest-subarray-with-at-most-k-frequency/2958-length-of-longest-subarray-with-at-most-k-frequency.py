# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(len(nums)):
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len