class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        left = [0]*n
        right = [0]*n
        current = 0
        for i in range(n):
            current = max(current, height[i])
            left[i] = current
        current = 0
        for i in range(n-1,-1,-1):
            current = max(current, height[i])
            right[i] = current
        total = 0
        for i in range(n):
            total += min(left[i],right[i])-height[i]
        return total

