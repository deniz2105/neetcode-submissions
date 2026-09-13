class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()
        i =0
        j =0
        while i < len(slots1) and j < len(slots2):
            if(slots1[i][0] < slots2[j][1] and slots2[j][0] < slots1[i][1]):
                overlappingInterval = [max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])]
                if overlappingInterval[1] - overlappingInterval[0] >= duration:
                    overlappingInterval[1] = overlappingInterval[0] + duration
                    return overlappingInterval
            
            if slots1[i][1] < slots2[j][1]:
                i +=1
            else:
                j+=1
        return []
                
