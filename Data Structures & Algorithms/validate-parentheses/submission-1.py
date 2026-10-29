class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(','}':'{',']':'['}
        for i in s:
            if i in d: #closing braket
                if not stack or d[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
