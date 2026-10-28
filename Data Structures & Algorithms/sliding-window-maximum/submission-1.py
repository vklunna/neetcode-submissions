class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # start = 0
        # stop = k
        # max_l = []
        # for i in range(len(nums)-k+1):
        #     now_l = nums[start:stop]
        #     max_l.append(max(now_l))
        #     start += 1
        #     stop +=1
        # return max_l
        dq=deque() #stores posiitons of nums
        result = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0]<=i-k:
                dq.popleft()
            if i>=k-1:
                result.append(nums[dq[0]])
        return result

