class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

# EXAMPLE

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6


