class UnionFind:
    def __init__(self, n):
        self.parents = []
        for i in range(n):
            self.parents.append(i)
        self.sizes = [1] * n

    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x,y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.sizes[px] > self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        return True



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return False
        
        val = uf.find(0)
        for i in range(1,n):
            if uf.find(i) != val:
                return False
        return True

        