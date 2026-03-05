class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = [0]*26
            
            for j in range(i,n):
                freq[ord(s[j]) - ord('a')] += 1
                
                mx = max(freq)
                mn = min([f for f in freq if f > 0])
                
                ans += mx - mn
                
        return ans