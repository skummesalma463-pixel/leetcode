class Solution:
    def isHappy(self, n: int) -> bool:
        # while n != 1 and n != 4:
        #     s = 0
        #     while n > 0:
        #         s += (n % 10) ** 2
        #         n //= 10
        #     n = s
        # return n == 1
        seen=set()
        while n !=1 and n not in seen:
            seen.add(n)
            n=sum(int(d)**2 for d in str(n))
        return n==1