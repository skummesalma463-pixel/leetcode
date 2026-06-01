class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # total=0
        # for i in range(1,num):
        #     if num%i==0:
        #         total +=i
        # return total==num

        # s=1
        # if num ==1:
        #     return False
        # for i in range(2,int(num**0.5)+1):
        #     if num%i==0:
        #         s +=(i+num//i)
        # return num==s
        return num in{6,28,496,8128,33550336}