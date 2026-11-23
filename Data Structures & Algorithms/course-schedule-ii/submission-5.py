class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjDict = defaultdict(list)
        indegree = [0] * numCourses

        for prereq in prerequisites:
            adjDict[prereq[1]].append(prereq[0])
            indegree[prereq[0]] +=1
        q = deque()
        path = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            currCourse = q.popleft()
            path.append(currCourse)

            if currCourse not in adjDict:
                continue
            
            for nextCourse in adjDict[currCourse]:
                indegree[nextCourse]-=1
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        if len(path) == numCourses:
            return path
        else:
            return []
        

