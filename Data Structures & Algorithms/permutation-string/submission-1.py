class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # left = 0
        # l = len(s1)
        # for i in range(len(s2)):
        #     if Counter(s1)==Counter(s2[left:l]):
        #         return True
        #     else:
        #         left+=1
        #         l+=1
        # return False
        m = len(s1)
        if m>len(s2):
            return False
        need = {}
        for c in s1:
            if c in need:
                need[c]+=1
            else:
                need[c]=1
        count = {}
        for c in s2[:m]:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
        if need ==count:
            return True
        for right in range(m, len(s2)):
            new = s2[right]
            if new in count:
                count[new]+=1
            else:
                count[new]=1
            old = s2[right-m]
            count[old]-=1
            if count[old]==0:
                del count[old]
            if need ==count:
                return True
        return False
        
