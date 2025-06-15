
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = Counter(nums)
        for num in k:
            if k[num] == 1:
                return num
