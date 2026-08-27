class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count1 = 1
        maxCount1 = 1
        count2 = 1
        maxCount2 = 1
        for i in range(len(arr)-1):
            if i % 2 == 1 and arr[i] > arr[i+1]:
                count1 +=1
                maxCount2 = max(maxCount2, count2)
                maxCount1 = max(maxCount1, count1)
                count2 = 1
            elif i % 2 == 0 and arr[i] < arr[i+1]:
                count1 +=1
                maxCount2 = max(maxCount2, count2)
                maxCount1 = max(maxCount1, count1)
                count2 = 1
            elif i % 2 == 0 and arr[i] > arr[i+1]:
                count2 +=1
                maxCount2 = max(maxCount2, count2)
                maxCount1 = max(maxCount1, count1)
                count1 = 1
            elif i % 2 == 1 and arr[i] < arr[i+1]:
                count2 +=1
                maxCount2 = max(maxCount2, count2)
                maxCount1 = max(maxCount1, count1)
                count1 = 1
            else:
                maxCount1 = max(maxCount1, count1)
                count1 = 1
                maxCount2 = max(maxCount2, count2)
                count2 = 1
        
        return max(maxCount1, maxCount2)
                 
