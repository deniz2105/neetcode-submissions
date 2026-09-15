class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort(key=lambda x:x[1])
        secondList.sort(key=lambda x:x[1])

        i = 0
        j = 0
        resp = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and secondList[j][0] <= firstList[i][1]:
                resp.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if secondList[j][1] > firstList[i][1]:
                i +=1
            else:
                j+=1
        return resp


