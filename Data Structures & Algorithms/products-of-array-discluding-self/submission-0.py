class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n=len(nums)
        left_list=[1]*n
        right_list = [1]*n
        for i in range(n):
            left_list[i]=left
            left*=nums[i]
        for i in range(n-1,-1,-1):
            right_list[i]=right
            right*=nums[i]
        answer = [1]*n
        for i in range(n):
            answer[i]=left_list[i]*right_list[i]
        return answer
