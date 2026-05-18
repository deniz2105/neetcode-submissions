class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lowIdx =0
        highIdx = len(numbers)-1
        high = numbers[highIdx]
        low = numbers[lowIdx]
        while lowIdx < highIdx:
            high = numbers[highIdx]
            low = numbers[lowIdx]
            if (high + low) == target:
                return [lowIdx+1, highIdx+1]
            if target - high > low:
                lowIdx +=1
            elif target - low < high:
                highIdx -= 1
        return [lowIdx+1, highIdx+1]
