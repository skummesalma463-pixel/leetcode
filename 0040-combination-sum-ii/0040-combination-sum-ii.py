class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def dfs(i,t,path):
            if t==0:
                ans.append(path[:])
                return
            if t<0:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>t:
                    break
                path.append(candidates[j])
                dfs(j+1,t-candidates[j],path)
                path.pop()
        dfs(0,target,[])
        return ans