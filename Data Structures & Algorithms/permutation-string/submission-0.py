class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        l = len(s1)
        for i in range(len(s2)):
            if Counter(s1)==Counter(s2[left:l]):
                return True
            else:
                left+=1
                l+=1
        return False
