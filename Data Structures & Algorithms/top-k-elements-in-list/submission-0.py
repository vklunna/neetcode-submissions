class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        list1=[]
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        list1=sorted(dict1, key = dict1.get, reverse = True)
        return list1[:k]