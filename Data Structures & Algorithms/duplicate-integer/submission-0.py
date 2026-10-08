class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = set()
        for i in nums:
            if i in new_list:
                return True
            new_list.add(i)
        return False