class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # suf[i] = the starting index in word1 for the suffix of word2 starting at index i
        # We compute this from right to left.
        suf = [-1] * (m + 1)
        suf[m] = n
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            # suf[j+1] will store the first index in word1 that matches word2[j+1:]
            # Let's store a boolean or precompute cleanly:
        
        # Let's rewrite using a standard suffix match array:
        match_suffix = [False] * (n + 1)
        # match_suffix[i] = True if word2 suffix can be matched starting at i
        # Actually, let's use `max_j_match[i]` = max suffix length of word2 matched from i.
        
        # Let's use the official editorial/accepted clean approach:
        # `next_match[i]` = can we match word2[i:] from word1?
        
        dp = [0] * (n + 1)
        # dp[i] = length of longest suffix of word2 that is a subsequence of word1[i:]
        curr = m - 1
        for i in range(n - 1, -1, -1):
            if curr >= 0 and word1[i] == word2[curr]:
                curr -= 1
            dp[i] = m - 1 - curr
            
        ans = []
        changed = False
        j = 0
        
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed:
                # Check if we can afford to change word1[i] to word2[j]
                # Meaning the rest of word2 (from j+1) can be matched by word1[i+1:]
                remaining_needed = m - (j + 1)
                if i + 1 < n and dp[i + 1] >= remaining_needed:
                    ans.append(i)
                    changed = True
                    j += 1
                    
        return ans if len(ans) == m else []