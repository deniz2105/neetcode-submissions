class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        count = 0
        j = 0
        for i in range(len(g)):
            while j < len(s):
                print(g[i])
                print(s[j])
                if g[i] <= s[j]:
                    count +=1
                    j+=1
                    break
                j+=1
        return count
