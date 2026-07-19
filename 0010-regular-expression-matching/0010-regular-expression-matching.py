class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1)for _ in range(m+1)]
        dp[m][n]=True
        for j in range(n-2,-1,-1):
            if p[j+1]=='*':
                dp[m][j]=dp[m][j+2]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                first=j<n and(p[j]==s[i]or p[j]=='.')
                if j+1<n and p[j+1]=='*':
                    dp[i][j]=dp[i][j+2]or(first and dp[i+1][j])
                else:
                    dp[i][j]=first and dp[i+1][j+1]
        return dp[0][0]