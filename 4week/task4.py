"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/count-primes/description/
"""


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime_tho = [True] * n
        prime_tho[0] = prime_tho[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime_tho[i]:
                for j in range(i * i, n, i):
                    prime_tho[j] = False

        return sum(prime_tho)
