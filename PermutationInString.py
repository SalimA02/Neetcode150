class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = sorted(s1)

        l1 = len(s1)
        l2 = len(s2)

        if sorted(s1) == sorted(s2):
            return True

        for i in range(l2-l1+1):
            if sorted(s2[i:i+l1]) == chars:
                return True
        return False
