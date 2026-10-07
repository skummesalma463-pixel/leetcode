class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            cnt = 0
            for char in string:
                if char == '(':
                    cnt += 1
                elif char == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in ('(', ')'):
                        next_level.add(item[:i] + item[i+1:])
            level = next_level