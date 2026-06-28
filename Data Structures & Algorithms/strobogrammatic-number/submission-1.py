class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        inverted = {}
        inverted['0'] = '0'
        inverted['1'] = '1'
        inverted['6'] ='9'
        inverted['8'] = '8'
        inverted['9'] = '6'
        j = len(num)-1
        i = 0
        while i <= j:
            if num[i] not in inverted or num[j] not in inverted:
                return False
            if num[i] != inverted[num[j]]:
                return False
            i +=1
            j -=1
        return True



    
