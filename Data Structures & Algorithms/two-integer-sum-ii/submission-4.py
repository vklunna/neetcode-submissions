class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left, right = 0, len(numbers)-1
        # while left<right:
        #     total = numbers[left]+numbers[right]
        #     if total == target:
        #         return [left+1, right+1]
        #     elif total < target:
        #         left+=1
        #     else:
        #         right -=1
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
                