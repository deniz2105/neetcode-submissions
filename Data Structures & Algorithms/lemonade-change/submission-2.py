class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        billsBank = {}
        billsBank[20] = 0
        billsBank[10] = 0
        billsBank[5] = 0
        
        

        for i in range(0,len(bills)):
            change = bills[i] - 5
            billsBank[bills[i]] +=1
            total += bills[i]
            if change > total:
                return False
            else:
                for key, value in billsBank.items():
                    while change >= key and billsBank[key] >0 and change > 0:
                        print("change" + str(change))
                        change -= key
                        billsBank[key] -=1
                print(change)
                if change != 0:
                    return False
        return True
