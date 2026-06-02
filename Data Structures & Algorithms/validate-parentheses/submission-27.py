class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for char in s:
            if char in '({[':
                stack.append(char)

            elif char in ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            
            elif char in '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()

            elif char in ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()

        return len(stack) == 0