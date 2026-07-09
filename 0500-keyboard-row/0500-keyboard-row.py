class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=set("qwertyuiopQWERTYUIOP")
        row2=set("asdfghjklASDFGHJKL")
        row3=set("zxcvbnmZXCVBNM")
        ans=[]
        for word in words:
            s=set(word)
            if s<=row1 or s<=row2 or s<=row3:
                ans.append(word)
        return ans