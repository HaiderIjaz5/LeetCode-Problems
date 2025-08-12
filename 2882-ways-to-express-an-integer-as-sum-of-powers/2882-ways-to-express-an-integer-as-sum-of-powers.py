class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        powers = []
        i = 1
        while i ** x <= n:
            powers.append(i ** x)
            i += 1

        # Step 2: dp[s] = number of ways to get sum s
        dp = [0] * (n + 1)
        dp[0] = 1  # 1 way to make sum 0 (pick nothing)

        # Step 3: For each power, update dp
        for p in powers:
            for s in range(n, p - 1, -1):  # go backward to avoid reuse
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]