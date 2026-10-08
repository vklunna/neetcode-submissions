class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        list1=[]
        for i in strs:
            key = "".join(sorted(i))
            if key not in dict1:
                dict1[key]=[]
            dict1[key].append(i)
        for i in dict1.values():
            list1.append(i)
        return list1
        
            
