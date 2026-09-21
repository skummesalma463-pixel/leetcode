class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = {}
        for num in nums:
            rem = num % k
            new_dp = {rem: 1}
            for prev_rem, count in dp.items():
                curr_rem = (prev_rem * rem) % k
                new_dp[curr_rem] = new_dp.get(curr_rem, 0) + count
            dp = new_dp
            for r, count in dp.items():
                res[r] += count
        return res