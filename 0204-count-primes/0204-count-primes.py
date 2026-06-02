class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)

    
        # count=0
        # for num in range(2,n):
        #     prime=True
        #     for i in range(2,num):
        #         if num%i==0:
        #             prime=False
        #             break

        #     if prime:
        #         count +=1
        # return count