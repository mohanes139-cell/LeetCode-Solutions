class ProductOfNumbers:

    def __init__(self):
        # Start with 1 as a neutral multiplier for prefix products
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A zero wipes out any product before it, so reset the list
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the current prefix length,
        # a 0 occurred within the last k elements
        if k >= len(self.prefix):
            return 0
        
        return self.prefix[-1] // self.prefix[-1 - k]