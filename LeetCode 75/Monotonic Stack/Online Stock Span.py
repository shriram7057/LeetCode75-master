class StockSpanner(object):

    def __init__(self):
        self.stack = []  # each element: (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        # Pop prices less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        # Push current price with total span
        self.stack.append((price, span))
        return span
