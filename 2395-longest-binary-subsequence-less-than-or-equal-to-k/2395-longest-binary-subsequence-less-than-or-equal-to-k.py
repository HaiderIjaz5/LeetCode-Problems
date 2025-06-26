class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
            n = len(s)
            count = 0
            value = 0
            power = 1

            for i in range(n - 1, -1, -1):
                if s[i] == '0':
                    count += 1
                else:
                    if power <= k and value + power <= k:
                        value += power
                        count += 1
                power <<= 1

            return count