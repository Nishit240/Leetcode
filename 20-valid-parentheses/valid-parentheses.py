class Solution(object):
    def isValid(self, s):
        """
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
            return True

            if ")(" in s or "}{" in s or "][" in s:
                return False
        return False
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0

        