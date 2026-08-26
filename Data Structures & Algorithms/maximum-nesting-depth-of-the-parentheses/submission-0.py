class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        maxDepth = 0

        for c in s:
            if c == '(':
                curr +=1
                maxDepth = max(maxDepth, curr)
            elif c == ')':
                curr -=1
            else:
                continue
        return maxDepth
