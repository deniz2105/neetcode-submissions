class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def sortString(s: str) -> str:
            sArr = [c for c in s]
            sArr.sort()
            return ''.join(sArr)

        l =0
        s1Sorted = sortString(s1)
        for r in range(len(s1)-1,len(s2)):
            ss = sortString(s2[l:r+1])
            print(ss)
            if ss == s1Sorted:
                return True
            else:
                l += 1

        return False

