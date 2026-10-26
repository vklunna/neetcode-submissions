class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        need = {}
        for i in t:
            need[i]=1+need.get(i,0)
        count = {}
        left=0
        best_len=len(s)+1
        best_start = 0
        def valid(count,need):
                for i in need:
                    if count.get(i,0)<need[i]:
                        return False
                return True
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while valid(count, need):
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_start=left
                count[s[left]]-=1
                left+=1
        if best_len==len(s)+1:
            return ""
        else:
            return s[best_start:best_start+best_len]
