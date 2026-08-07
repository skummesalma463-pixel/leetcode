class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        kFactorCounts = {
            0: {},
            1: {},
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2}
        }

        def get_prime_count_t(val):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while val % p == 0:
                    val //= p
                    count[p] += 1
            return count, val == 1

        prime_count, is_divisible = get_prime_count_t(t)
        if not is_divisible:
            return "-1"

        def get_factor_count(count):
            c2, c3, c5, c7 = count.get(2, 0), count.get(3, 0), count.get(5, 0), count.get(7, 0)
            count8 = c2 // 3
            rem2 = c2 % 3
            count9 = c3 // 2
            rem3 = c3 % 2
            count4 = rem2 // 2
            count2 = rem2 % 2

            count6 = 0
            if count2 == 1 and rem3 == 1:
                count2 = 0
                rem3 = 0
                count6 = 1
            if rem3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                rem3 = 0
                count4 = 0

            res = {2: count2, 3: rem3, 4: count4, 5: c5, 6: count6, 7: c7, 8: count8, 9: count9}
            return res

        factor_count = get_factor_count(prime_count)
        
        def sum_values(d):
            return sum(d.values())

        def construct(factors):
            res = []
            for digit in range(2, 10):
                res.extend([str(digit)] * factors.get(digit, 0))
            return "".join(res)

        # If required digits take more length than num, we must increase length by padding with '1's
        if sum_values(factor_count) > len(num):
            return "1" * (len(num) + 1 - sum_values(factor_count) if False else 0) + construct(factor_count)
            # Alternatively: padding zeros/ones up to len(num) + 1 if needed:
            # Let's write it cleanly below:

        def get_prime_count_num(s):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for ch in s:
                for prime, freq in kFactorCounts[int(ch)].items():
                    count[prime] += freq
            return count

        prime_count_prefix = get_prime_count_num(num)
        first_zero_index = num.find('0')
        if first_zero_index == -1:
            first_zero_index = len(num)
            ok = True
            for k in prime_count:
                if prime_count_prefix.get(k, 0) < prime_count[k]:
                    ok = False
                    break
            if ok:
                return num

        def subtract(a, b):
            res = a.copy()
            for k, v in b.items():
                res[k] = res.get(k, 0) - v
            return res

        n = len(num)
        
        # If length needs to increase by 1 right away because sum of required factors > n
        if sum_values(factor_count) > n:
            return "1" * (n + 1 - sum_values(factor_count)) + construct(factor_count) if sum_values(factor_count) <= n + 1 else construct(factor_count) # simplified below:

        for i in range(n - 1, -1, -1):
            d = int(num[i])
            for prime, freq in kFactorCounts[d].items():
                prime_count_prefix[prime] -= freq

            space_after = n - 1 - i
            if i > first_zero_index:
                continue

            for bigger_digit in range(d + 1, 10):
                rem_prime = subtract(prime_count, prime_count_prefix)
                for p in rem_prime:
                    rem_prime[p] = max(0, rem_prime[p] - kFactorCounts[bigger_digit].get(p, 0))
                
                factors_after = get_factor_count(rem_prime)
                if sum_values(factors_after) <= space_after:
                    fill_ones = space_after - sum_values(factors_after)
                    return num[:i] + str(bigger_digit) + "1" * fill_ones + construct(factors_after)

        # Fallback to length n + 1
        return "1" * (n + 1 - sum_values(factor_count)) + construct(factor_count)