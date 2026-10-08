class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = 1
        # right = 1
        # n=len(nums)
        # left_list=[1]*n
        # right_list = [1]*n
        # for i in range(n):
        #     left_list[i]=left
        #     left*=nums[i]
        # for i in range(n-1,-1,-1):
        #     right_list[i]=right
        #     right*=nums[i]
        # answer = [1]*n
        # for i in range(n):
        #     answer[i]=left_list[i]*right_list[i]
        # return answer
        list1=[]
        prod=1
        zero_count=0
        for i in nums:
            if i==0:
                zero_count+=1     
            else:
                prod*=i
        for i in nums:
            if zero_count>=2:
                list1.append(0)
            elif zero_count==1:
                if i==0:
                    list1.append(int(prod))
                else:
                    list1.append(0)
            else:   
                list1.append(int(prod/i))
        return list1
