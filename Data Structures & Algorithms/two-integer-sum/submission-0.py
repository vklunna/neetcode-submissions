class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        dict1={}
        for i,num in enumerate(nums):
            find = target - num
            if find in dict1:
                indices.append(dict1[find])
                indices.append(i)
            else:
                dict1[num]=i
        return indices
