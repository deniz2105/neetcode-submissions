class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = []

        for i in range(len(customers)):
            s.append(customers[i] * grumpy[i])
        
        maxC = 0
        for i in range(minutes):
            maxC += s[i]
        curr = maxC
        for i in range(minutes, len(s)):
            curr = curr + s[i] - s[i-minutes]
            maxC = max(maxC, curr)
        print(maxC)
        print(s)
        
        totalCustomers = sum(customers)
        print(totalCustomers)
        totalDisgruntled = sum(s) - maxC
        return totalCustomers - totalDisgruntled

