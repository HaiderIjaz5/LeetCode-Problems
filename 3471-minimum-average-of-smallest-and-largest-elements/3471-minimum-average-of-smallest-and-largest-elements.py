class Solution:
    def minimumAverage(self, nums: list) -> float:
        averages = []

        # Repeat until nums becomes empty
        while len(nums) > 1:
            # Find the smallest and largest elements manually
            minElement = nums[0]
            maxElement = nums[0]
            
            for num in nums:
                if num < minElement:
                    minElement = num
                if num > maxElement:
                    maxElement = num
            
            # Add their average to the averages list
            averages.append((minElement + maxElement) / 2)

            # Remove one occurrence of minElement and maxElement manually
            new_nums = []
            minRemoved = False
            maxRemoved = False

            for num in nums:
                if num == minElement and not minRemoved:
                    minRemoved = True
                elif num == maxElement and not maxRemoved:
                    maxRemoved = True
                else:
                    new_nums.append(num)
            
            nums = new_nums

        # Find the smallest value in averages manually
        minAverage = averages[0]
        for avg in averages:
            if avg < minAverage:
                minAverage = avg
        
        return minAverage