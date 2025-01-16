class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[i](operand1, operand2)
                stack.append(result)

        return stack[0]
