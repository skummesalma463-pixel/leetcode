class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num+=1<<32
        h="0123456789abcdef"
        r=""
        while num:
            r=h[num&15]+r
            num>>=4
        return r