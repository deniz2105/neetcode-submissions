class Solution:
    def isValid(self, s: str) -> bool:
        ps = {}
        ps['('] = ')'
        ps['{'] = '}'
        ps['['] = ']'

        ss = deque()
        for i in range(0, len(s)):
            if s[i] in ps:
                ss.append(s[i])
            elif len(ss) == 0 or s[i] != (ps[ss.pop()]):
                return False
        
        return len(ss) == 0
        
