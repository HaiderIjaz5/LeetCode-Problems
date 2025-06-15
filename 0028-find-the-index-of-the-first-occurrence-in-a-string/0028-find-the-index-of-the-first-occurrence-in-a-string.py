class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):  # Only go up to where needle can fit
            if haystack[i:i + m] == needle:
                return i
        return -1