class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []
         
        for i in nums:
            if i in numbers:
                return True
            else:
                numbers.append(i)
        return False
