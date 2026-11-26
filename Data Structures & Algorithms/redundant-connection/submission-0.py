class UnionFind:
    def __init__(self,n):
        self.parents = []
        for i in range(n):
            self.parents.append(i)
        self.sizes = [1] * n
    
    def find(self, x):
        if self.parents[x] !=x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x,y):
        px, py = self.find(x), self.find(y)

        if self.parents[x] == self.parents[y]:
            return False
        
        if self.sizes[px] > self.sizes[py]:
            self.sizes[px] += self.sizes[py]
            self.parents[py] = px
        else:
            self.sizes[py] += self.sizes[px]
            self.parents[px] = py
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for edge in edges:
            
            if not uf.union(edge[0]-1,edge[1]-1):
                return edge
        return []



        