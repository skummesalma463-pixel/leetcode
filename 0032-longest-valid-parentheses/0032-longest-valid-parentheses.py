class Solution:
    def longestValidParentheses(self,s:str)->int:
        st=[-1];mx=0
        for i,c in enumerate(s):
            if c=='(':st.append(i)
            else:
                st.pop()
                if not st:st.append(i)
                else:mx=max(mx,i-st[-1])
        return mx