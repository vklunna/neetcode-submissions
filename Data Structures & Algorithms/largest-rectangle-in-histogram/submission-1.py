class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n
        right = [n]*n

        stack=[]
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                j=stack.pop()
                right[j]=i
            stack.append(i)
        
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[i]<heights[stack[-1]]:
                j=stack.pop()
                left[j]=i
            stack.append(i)

        best = 0
        for i in range(n):
            width = right[i]-left[i]-1
            best = max(best, heights[i]*width)
        return best