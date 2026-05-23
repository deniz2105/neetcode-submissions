class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            prefix = "#" + str(len(s)) + "&"
            r += prefix + s
        return r


    def decode(self, s: str) -> List[str]:
        r = []
        currLen = ""
        idx = 0
        while idx < len(s):
            if s[idx] == "#":
                currLen = ""
                idx+=1
            elif s[idx] == "&":
                r.append(s[idx+1:idx+int(currLen)+1])
                idx= idx+int(currLen)+1
            elif idx != "#" or idx != "&" :
                currLen += s[idx]
                idx+=1
        return r
                
            
