class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        countt, streak = 0, 0
        for num in nums:
            if num == 0:
                streak += 1
                countt += streak
            else:
                streak = 0
        return countt