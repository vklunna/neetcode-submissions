class Solution:
    def trap(self, height: List[int]) -> int:
        # n= len(height)
        # left = [0]*n
        # right = [0]*n
        # current = 0
        # for i in range(n):
        #     current = max(current, height[i])
        #     left[i] = current
        # current = 0
        # for i in range(n-1,-1,-1):
        #     current = max(current, height[i])
        #     right[i] = current
        # total = 0
        # for i in range(n):
        #     total += min(left[i],right[i])-height[i]
        # return total

        l,r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        res = 0
        while l<r:
            if left_max<right_max:
                l+=1
                left_max = max(left_max, height[l])
                res += left_max-height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                res+=right_max-height[r]
        return res

