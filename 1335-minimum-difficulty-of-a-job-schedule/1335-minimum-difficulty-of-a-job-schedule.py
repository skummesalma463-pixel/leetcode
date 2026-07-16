class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jd=jobDifficulty
        n=len(jd)
        if n<d:
            return-1
        dp=[float("inf")]*n
        mx=0
        for i in range(n):
            mx=max(mx,jd[i])
            dp[i]=mx
        for day in range(1,d):
            ndp=[float("inf")]*n
            for i in range(day,n):
                mx=0
                for j in range(i,day-1,-1):
                    mx=max(mx,jd[j])
                    ndp[i]=min(ndp[i],dp[j-1]+mx)
            dp=ndp
        return dp[-1]