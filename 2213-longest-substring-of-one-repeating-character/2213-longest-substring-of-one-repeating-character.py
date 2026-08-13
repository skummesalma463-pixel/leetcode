# class Solution:
#     def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
class Solution:
    def longestRepeating(self,s:str,queryCharacters:str,queryIndices:List[int])->List[int]:
        n=len(s)
        s=list(s)
        tree=[0]*(4*n)
        pref=[0]*(4*n)
        suff=[0]*(4*n)
        lchar=['']*4*n
        rchar=['']*4*n
        def build(node,l,r):
            if l==r:
                tree[node]=pref[node]=suff[node]=1
                lchar[node]=rchar[node]=s[l]
                return
            mid=(l+r)//2
            build(2*node,l,mid)
            build(2*node+1,mid+1,r)
            pushup(node,mid-l+1,r-mid)
        def pushup(node,l_len,r_len):
            left=2*node
            right=2*node+1
            lchar[node]=lchar[left]
            rchar[node]=rchar[right]
            tree[node]=max(tree[left],tree[right])
            pref[node]=pref[left]
            if lchar[left]==lchar[right] and pref[left]==l_len:
                pref[node]+=pref[right]
            suff[node]=suff[right]
            if rchar[left]==rchar[right] and suff[right]==r_len:
                suff[node]+=suff[left]
            if rchar[left]==lchar[right]:
                tree[node]=max(tree[node],suff[left]+pref[right])
        def update(node,l,r,idx,val):
            if l==r:
                s[l]=val
                lchar[node]=rchar[node]=val
                return
            mid=(l+r)//2
            if idx<=mid:
                update(2*node,l,mid,idx,val)
            else:
                update(2*node+1,mid+1,r,idx,val)
            pushup(node,mid-l+1,r-mid)
        build(1,0,n-1)
        ans=[]
        for c,idx in zip(queryCharacters,queryIndices):
            update(1,0,n-1,idx,c)
            ans.append(tree[1])
        return ans