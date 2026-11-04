import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self):
        self.small = []       # Max heap
        self.large = []       # Min heap
        self.delay = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap, sign):
        while heap:
            x = sign * heap[0]

            if self.delay[x] > 0:
                self.delay[x] -= 1
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            x = -heapq.heappop(self.small)

            self.small_size -= 1
            self.large_size += 1

            self.small_sum -= x
            self.large_sum += x

            heapq.heappush(self.large, x)
            self.prune(self.small, -1)

        elif self.small_size < self.large_size:
            x = heapq.heappop(self.large)

            self.large_size -= 1
            self.small_size += 1

            self.large_sum -= x
            self.small_sum += x

            heapq.heappush(self.small, -x)
            self.prune(self.large, 1)

    def add(self, x):
        self.prune(self.small, -1)
        self.prune(self.large, 1)

        if not self.small or x <= -self.small[0]:
            heapq.heappush(self.small, -x)
            self.small_size += 1
            self.small_sum += x
        else:
            heapq.heappush(self.large, x)
            self.large_size += 1
            self.large_sum += x

        self.balance()

    def remove(self, x):
        self.prune(self.small, -1)
        self.prune(self.large, 1)

        self.delay[x] += 1

        if x <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= x

            if x == -self.small[0]:
                self.prune(self.small, -1)
        else:
            self.large_size -= 1
            self.large_sum -= x

            if self.large and x == self.large[0]:
                self.prune(self.large, 1)

        self.balance()

    def cost(self):
        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        n = len(nums)

        # Step 1: Calculate cost of every window of size x
        dh = DualHeap()
        costs = []

        for i in range(n):
            dh.add(nums[i])

            if i >= x:
                dh.remove(nums[i - x])

            if i >= x - 1:
                costs.append(dh.cost())

        # Step 2: Dynamic Programming
        inf = float('inf')

        dp = [[inf] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(n + 1):

            # Option 1: Skip current element
            if i < n:
                for j in range(k + 1):
                    dp[i + 1][j] = min(
                        dp[i + 1][j],
                        dp[i][j]
                    )

            # Option 2: Select a window of size x
            if i + x <= n:
                for j in range(1, k + 1):
                    dp[i + x][j] = min(
                        dp[i + x][j],
                        dp[i][j - 1] + costs[i]
                    )

        return dp[n][k]