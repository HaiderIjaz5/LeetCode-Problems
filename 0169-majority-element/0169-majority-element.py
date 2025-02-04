class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq_dict = {}  # Dictionary to store counts

        for num in nums:  
            freq_dict[num] = freq_dict.get(num, 0) + 1

       
        for num in nums:  
            if freq_dict[num] > n // 2:
                return num

        return 0
