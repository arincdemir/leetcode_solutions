class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        pointer = len(self.stocks) - 1
        while pointer >= 0 and self.stocks[pointer][0] <= price:
            pointer = self.stocks[pointer][1]
        
        self.stocks.append((price, pointer))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)