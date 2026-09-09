class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resp = []
        intervals.sort()

        i = 1
        curr = intervals[0]

        while i < len(intervals):
            if curr[1] < intervals[i][0]:
                resp.append(curr)
                curr = intervals[i]
                i+=1
            else:
                curr[0] = min(curr[0], intervals[i][0])
                curr[1] = max(curr[1], intervals[i][1])
                i+=1
        resp.append(curr)
        return resp



