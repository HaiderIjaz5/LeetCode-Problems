class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value=max(nums)
        max_len=0
        current_len=0
        for i in nums:
            if i==max_value:
                current_len+=1
                max_len=max(max_len,current_len)
            else:
                current_len=0
        return max_len