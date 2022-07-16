# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brace = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closing_brace:
                if stack and stack[-1] == closing_brace[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
