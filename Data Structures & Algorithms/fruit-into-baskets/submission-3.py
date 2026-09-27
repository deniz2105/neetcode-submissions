class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fs = {}
        fp = 0
        sp = 0
        maxLen = 1

        while fp >= sp and  fp < len(fruits):
            if fruits[fp] not in fs:
                fs[fruits[fp]]= 1
            else:
                fs[fruits[fp]]+= 1
            print(fs)
            while len(fs.items()) > 2 and fp >= sp:
                
                fs[fruits[sp]]-= 1
                if fs[fruits[sp]] == 0:
                    del fs[fruits[sp]]
                sp+=1
            maxLen = max(maxLen, fp - sp + 1)
            fp +=1
        
        return maxLen
