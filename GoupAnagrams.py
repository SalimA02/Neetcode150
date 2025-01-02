class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []
        for i in strs:
            if ''.join(sorted(i)) in hashmap:
                hashmap[''.join(sorted(i))].append(i)
            else:
                hashmap[''.join(sorted(i))] = [i]
        # print(hashmap)

        result = list(hashmap.values())
        print(result)
        return result
