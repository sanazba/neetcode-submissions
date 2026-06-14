class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = { "(" : ")", "[" : "]", "{" : "}" }
        stack = []

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            elif not stack or c != stack.pop():
                return False

        return not stack