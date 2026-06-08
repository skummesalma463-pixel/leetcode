class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum
        total_sum = sum(cardPoints)
        for i in range(window_size, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)
        return total_sum - min_window_sum