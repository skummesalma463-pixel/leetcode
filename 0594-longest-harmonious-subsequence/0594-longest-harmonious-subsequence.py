class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxLength = 0

        for num in freq:
            if num + 1 in freq:
                maxLength = max(maxLength, freq[num] + freq[num + 1])

        return maxLength