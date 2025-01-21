class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tupleList = result = list(zip(position, speed))
        tupleList = sorted(tupleList, key=lambda x: x[0])
        print(tupleList)

        stack = []
        for p, s in tupleList[::-1]:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

            
