class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s)).lower()

        start = 0
        end = len(s)-1

        while end >= start:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True
