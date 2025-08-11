class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        power = 1
        MOD = 10**9 + 7

        # Find highest power of 2 <= n
        while power <= n:
            power <<= 1
        power >>= 1

        # Build powers list
        powers = []
        temp_n = n
        while temp_n > 0:
            if power <= temp_n:
                powers.append(power)
                temp_n -= power
            power >>= 1

        size = len(powers)
        
        # Build prefix 2D array
        prefix = [[0] * size for _ in range(size)]
        for i in range(size):
            prefix[i][i] = powers[size - 1 - i]
            for j in range(i + 1, size):
                prefix[i][j] = (prefix[i][j - 1] * powers[size - 1 - j]) % MOD

        # Answer queries
        res = []
        for l, r in queries:
            res.append(prefix[l][r])

        return res
