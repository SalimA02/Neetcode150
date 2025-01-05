class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1 
        # print(freq)
        # print(len(freq))

        for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]:
            result.append(key)
        return(result)
