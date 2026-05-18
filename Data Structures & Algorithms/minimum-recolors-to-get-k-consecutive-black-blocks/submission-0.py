class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wb = {}
        wb['W'] = 0
        minW = 101
        wb['B'] = 0
        counter = 0
        for i in range(0, len(blocks)):
            wb[blocks[i]] +=1
            counter+=1
            if counter > k:
                wb[blocks[i -k]] -= 1
                if wb['W'] < minW:
                    minW = wb['W']
        
        if wb['W'] < minW:
            minW = wb['W']
        
        return minW
        