import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        # Priority queue stores: (distance, node, count of consecutive current node's label)
        # When starting at node 0, the initial count of its label is 1.
        pq = [(0, 0, 1)]
        dist = {}
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
            
            if (u, count) in dist and dist[(u, count)] < d:
                continue
            
            for v, w in adj[u]:
                nxt_char = labels[v]
                curr_char = labels[u]
                
                if nxt_char == curr_char:
                    nxt_count = count + 1
                else:
                    nxt_count = 1
                
                if nxt_count <= k:
                    if (v, nxt_count) not in dist or d + w < dist[(v, nxt_count)]:
                        dist[(v, nxt_count)] = d + w
                        heapq.heappush(pq, (d + w, v, nxt_count))
                        
        return -1