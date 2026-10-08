class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = ['']*len(s)
        s = s.lower().strip()
        s = re.sub('[^A-Za-z0-9]+', '', s)
        for i,char in enumerate(s):
            list1[-i-1]=char
        new_str = "".join(list1)
        if new_str == s:
            return True
        return False