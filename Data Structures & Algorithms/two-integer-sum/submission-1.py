class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        dict1={}
        for i,num in enumerate(nums):
            find = target - num
            if find in dict1:
                return [dict1[find],i]
            dict1[num]=i
       
