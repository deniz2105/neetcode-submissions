class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqDict = defaultdict(list)

        for i in range(len(prerequisites)):
            prereqDict[prerequisites[i][0]].extend(prerequisites[i][1:])
        canTake = set()
        def dfs(course, visited):
            if course in visited:
                return False
            visited.add(course)
            if course not in prereqDict:
                visited.remove(course)
                return True
            
            canPass = True
            for p in prereqDict[course]:
                if p in canTake:
                    continue
                else:
                    if not dfs(p, visited):
                        return False
                print(canPass)
                print(p)
            visited.remove(course)
            canTake.add(course)

            return True

        for i in range(numCourses):
            print(i)
            visited = set()
            if i in canTake:
                continue
            if not dfs(i, visited):
                return False
                

        return True

