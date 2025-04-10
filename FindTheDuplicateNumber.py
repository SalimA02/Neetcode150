class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        contact = 0

        while True:
            slow = nums[slow]
            contact = nums[contact]
            if slow == contact:
                return contact
