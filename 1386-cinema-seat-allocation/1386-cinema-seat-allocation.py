from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] |= (1 << (s - 2))
        
        ans = (n - len(rows)) * 2
        for mask in rows.values():
            left = (mask & 0b11110000) == 0
            right = (mask & 0b00001111) == 0
            middle = (mask & 0b00111100) == 0
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        return ans