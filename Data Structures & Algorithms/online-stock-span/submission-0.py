class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices)-1
        resp = 0
        while i >= 0 and self.prices[i] <= price:
            resp+=1
            i-=1
        return resp

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)