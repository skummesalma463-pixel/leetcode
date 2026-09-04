class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Build the suffix minimum array
        suffix_min = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suffix_min[i] = current_min
            
        # Step 2: Iterate and maintain running prefix maximum
        curr_max = float('-inf')
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
                
            # Check instability score
            if curr_max - suffix_min[i] <= k:
                return i
                
        return -1