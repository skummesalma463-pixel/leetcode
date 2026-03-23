class Solution:
    def reverse(self,x:int)->int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        x=str(x)
        x=x[::-1]
        x=int(x)
        x=x*sign
        if x<-2**31 or x>2**31-1:
            return 0
        return x