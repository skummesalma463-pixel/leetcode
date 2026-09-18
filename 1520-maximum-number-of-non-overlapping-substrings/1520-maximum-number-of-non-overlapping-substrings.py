class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = {c: n for c in set(s)}
        right = {c: -1 for c in set(s)}
        for i, c in enumerate(s):
            left[c] = min(left[c], i)
            right[c] = max(right[c], i)
        
        def get_valid_substring(i):
            r = right[s[i]]
            j = i
            while j <= r:
                c = s[j]
                if left[c] < i:
                    return -1
                r = max(r, right[c])
                j += 1
            return r

        intervals = []
        for i in range(n):
            if i == left[s[i]]:
                end = get_valid_substring(i)
                if end != -1:
                    intervals.append((end, i))
        
        intervals.sort()
        res = []
        last_end = -1
        for end, start in intervals:
            if start > last_end:
                res.append(s[start:end + 1])
                last_end = end
        return res