class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=len(digits)-1
        while x>=0:
            if(digits[x]<9):
                digits[x]+=1
                return digits
            else:
                digits[x]=0
            x-=1
        return [1]+digits
            
