class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        list1=[]
        for i, num in enumerate(nums):
            if i!=0 and num==nums[i-1]:
                continue
            target = -1*num
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[left]+nums[right]
                if s> target:
                    right -=1
                elif s<target:
                    left+=1
                else:
                    list1.append([num, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return list1