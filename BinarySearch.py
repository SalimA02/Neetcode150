class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2
        
        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)


###### BUILT IN FUNCTION ######
# import bisect
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         index = bisect.bisect_left(nums, target)
#         return index if index < len(nums) and nums[index] == target else -1
