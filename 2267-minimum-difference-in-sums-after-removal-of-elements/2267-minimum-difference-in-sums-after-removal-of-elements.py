class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # Prefix max heap: smallest possible sum of first n elements
        left_sum = sum(nums[:n])
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        
        left = [0] * (len(nums))
        left[n-1] = left_sum
        
        for i in range(n, 2*n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)
            left[i] = left_sum
        
        # Suffix min heap: largest possible sum of last n elements
        right_sum = sum(nums[2*n:])
        min_heap = nums[2*n:]
        heapq.heapify(min_heap)
        
        right = [0] * (len(nums))
        right[2*n] = right_sum
        
        for i in range(2*n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)
            right[i] = right_sum
        
        # Compute minimum difference
        result = float('inf')
        for i in range(n - 1, 2*n):
            result = min(result, left[i] - right[i + 1])
        
        return result