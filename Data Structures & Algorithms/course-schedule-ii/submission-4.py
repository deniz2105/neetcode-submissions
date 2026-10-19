class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseDict = {}

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in courseDict:
                courseDict[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                 courseDict[prerequisites[i][0]].append(prerequisites[i][1])
        

        path = []
        completed = set()
        def dfs(visited, curr, currPath):
            if curr in completed:
                return currPath
            if curr not in courseDict:
                currPath.append(curr)
                completed.add(curr)
                return currPath
            if curr in visited:
                return [-1]
            
            visited.add(curr)
            prereqs = courseDict[curr]

            for p in prereqs:
                np = dfs(visited, p, [])
                if -1 in np:
                    return [-1]
                currPath.extend(np)
            visited.remove(curr)
            currPath.append(curr)
            completed.add(curr)
            return currPath


        for i in range(numCourses):
            if i in completed:
                continue
            elif i not in courseDict:
                path.append(i)
            else:
                currPath = dfs(set(), i, [])
                if -1 in currPath:
                    return []
                path.extend(currPath)
        return path
                



        
