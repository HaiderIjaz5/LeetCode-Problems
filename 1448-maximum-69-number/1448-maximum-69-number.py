class Solution:
    def maximum69Number (self, num: int) -> int:
        t=str(num).replace('6', '9', 1)
        return int(t)