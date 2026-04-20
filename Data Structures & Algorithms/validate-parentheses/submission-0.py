class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for each_char in s:
            if each_char in '([{':
                stack.append(each_char)
            else:
                if len(stack) == 0:
                    return False
                last_char = stack[-1]
                if last_char == '(' and each_char == ')':
                    stack.pop()
                elif last_char == '[' and each_char == ']':
                    stack.pop()
                elif last_char == '{' and each_char == '}':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0