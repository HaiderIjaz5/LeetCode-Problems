class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        positions = [pos for pos, _ in fruits]
        amounts = [amt for _, amt in fruits]
        n = len(fruits)
        
        # Prefix sum for range query
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + amounts[i]

        def get_fruit(l, r):
            return prefix[r + 1] - prefix[l]

        res = 0

        # Go left then right
        for left_steps in range(k + 1):
            left = startPos - left_steps
            right_steps = k - 2 * left_steps
            right = startPos + max(0, right_steps)

            l = bisect_left(positions, left)
            r = bisect_right(positions, right) - 1
            if l <= r:
                res = max(res, get_fruit(l, r))

        # Go right then left
        for right_steps in range(k + 1):
            right = startPos + right_steps
            left_steps = k - 2 * right_steps
            left = startPos - max(0, left_steps)

            l = bisect_left(positions, left)
            r = bisect_right(positions, right) - 1
            if l <= r:
                res = max(res, get_fruit(l, r))

        return res