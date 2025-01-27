class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)
        
        if length < 3:
            return []
          
        r = length - 1

        for l in range(r):
            for j in range(r, l, -1):
                if (0 - nums[l] - nums[j]) in nums[l+1:j] and sorted([nums[l], nums[j], (0 - nums[l] - nums[j])]) not in output:
                    output.append(sorted([nums[l], nums[j], (0 - nums[l] - nums[j])]))
        return output
