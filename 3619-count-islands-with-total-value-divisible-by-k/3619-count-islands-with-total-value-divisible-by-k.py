class Solution:
    def countIslands(self,grid:List[List[int]],k:int)->int:
        m,n=len(grid),len(grid[0])
        v=set()
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0 and(i,j) not in v:
                    s,q=0,[(i,j)]
                    v.add((i,j))
                    while q:
                        r,col=q.pop(0)
                        s+=grid[r][col]
                        for nr,nc in((r+1,col),(r-1,col),(r,col+1),(r,col-1)):
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]>0 and(nr,nc) not in v:
                                v.add((nr,nc))
                                q.append((nr,nc))
                    if s%k==0:
                        c+=1
        return c