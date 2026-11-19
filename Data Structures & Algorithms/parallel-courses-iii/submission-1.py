class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqs = {}

        for relation in relations:
            if relation[1]-1 in prereqs:
                prereqs[relation[1]-1].append(relation[0]-1)
            else:
                prereqs[relation[1]-1] = [relation[0]-1]
        courseTotalTime = {}

        def dfs(course):
            if course in courseTotalTime:
                return courseTotalTime[course]
            if course not in prereqs:
                courseTotalTime[course] = time[course]
                return time[course]
            maxLen = float('-inf')
            for prereq in prereqs[course]:
                maxLen = max(maxLen, dfs(prereq))
            courseTotalTime[course] = maxLen + time[course]
            return courseTotalTime[course]
        maxLen = float('-inf')
        for i in range(n):
            maxLen = max(maxLen, dfs(i))
        return maxLen

