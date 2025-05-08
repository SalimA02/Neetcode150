class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = []
        longest  = 0 
        l,r = 0,0

        while l < len(s):
            for r in range(l, len(s)):
                if s[r] in characters:
                    characters = []
                    l += 1
                else:
                    characters.append(s[r])
                    longest = max(longest, len(characters))
        return longest


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             charSet = set()
#             for j in range(i, len(s)):
#                 if s[j] in charSet:
#                     break
#                 charSet.add(s[j])
#             res = max(res, len(charSet))
#         return res
