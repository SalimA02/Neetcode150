class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            restOfArray = temperatures[i+1:]
            for x in range(len(restOfArray)):
                if restOfArray[x] > temperatures[i]:
                    output.append(x+1)
                    break
                elif restOfArray[x] <= temperatures[i] and x == len(restOfArray)-1:
                    output.append(0)
        output.append(0)
        return output
# Time Complexity: O(n^2), will update with more efficient solution
