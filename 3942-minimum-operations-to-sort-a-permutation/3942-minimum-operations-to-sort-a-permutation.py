from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper to find valid target states (type, shift) where array is sorted
        def get_target_states(arr):
            res = set()
            # Type 0: rotation of original array
            idx = arr.index(0) if 0 in arr else -1
            if idx != -1:
                if all(arr[(idx + i) % n] == i for i in range(n)):
                    res.add((0, idx))
                    
            # Type 1: rotation of reversed original array
            rev = arr[::-1]
            idx = rev.index(0) if 0 in rev else -1
            if idx != -1:
                if all(rev[(idx + i) % n] == i for i in range(n)):
                    res.add((1, idx))
            return res

        target_states = get_target_states(nums)
        if not target_states:
            return -1
            
        # BFS on the 2n state graph
        queue = deque([(0, 0, 0)])  # (type, shift, distance)
        visited = {(0, 0)}
        
        while queue:
            t, s, d = queue.popleft()
            if (t, s) in target_states:
                return d
                
            # Operation 1: Rotate Left by One
            nt, ns = t, (s + 1) % n
            if (nt, ns) not in visited:
                visited.add((nt, ns))
                queue.append((nt, ns, d + 1))
                
            # Operation 2: Reverse the entire array
            nt, ns = 1 - t, (n - s) % n
            if (nt, ns) not in visited:
                visited.add((nt, ns))
                queue.append((nt, ns, d + 1))
                
        return -1