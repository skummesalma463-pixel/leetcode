class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        rev=s[::-1]
        if rev==s:
            return True
        else:
            return False