MOD = 10**9 + 7
MAX = 100005  # max n

# Precompute factorials and inverse factorials
fact = [1] * MAX
inv_fact = [1] * MAX

# Precompute factorials
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# Fast power mod
def mod_pow(a, b):
    result = 1
    while b:
        if b % 2:
            result = result * a % MOD
        a = a * a % MOD
        b //= 2
    return result

# Compute inverse factorials using Fermat's little theorem
inv_fact[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# Binomial coefficient
def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Using the formula: m × C(n-1, k) × (m-1)^(n-1-k)
        c = comb(n - 1, k)
        pow_term = mod_pow(m - 1, n - 1 - k)
        return m * c % MOD * pow_term % MOD
