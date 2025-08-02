class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        total_count = count1 + count2
        for val in total_count:
            if total_count[val] % 2 != 0:
                return -1
        
        excess1, excess2 = [], []
        for val in total_count:
            diff = count1[val] - total_count[val] // 2
            if diff > 0:
                excess1.extend([val] * diff)
            elif diff < 0:
                excess2.extend([val] * (-diff))
        
        excess1.sort()
        excess2.sort(reverse=True)
        
        min_global = min(min(basket1), min(basket2))
        cost = 0
        
        for a, b in zip(excess1, excess2):
            cost += min(min(a, b), 2 * min_global)
        
        return cost
