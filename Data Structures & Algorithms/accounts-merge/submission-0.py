class UnionFind:
    def __init__(self, n):
        self.ranks = [1] * n
        self.parents = []
        for i in range(n):
            self.parents.append(i)
    def find(self, x):
        if self.parents[x] != x:
            x = self.find(self.parents[x])
        return x
    
    def union(self, x, y):
        parent1, parent2 = self.find(x), self.find(y)
        if parent1 == parent2:
            return False
        if self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent1] = parent2
        elif self.ranks[parent2] > self.ranks[parent1]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] +=1

            
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailDict = {}

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in emailDict:
                    uf.union(i, emailDict[email])
                else:
                    emailDict[email] = i
        emailAccounts = defaultdict(list)
        for k,v in emailDict.items():
            leader = uf.find(v)
            emailAccounts[leader].append(k)
        resp = []
        for k,v in emailAccounts.items():
            name = accounts[k][0]
            resp.append([name]+sorted(v))
        return resp
        
        