class Stock:
    def __init__(self, name, prices: dict):
        self.name = name
        self.prices = prices

    def __str__(self):
        return f'{self.name}'
    
    def price(self, date):
        return self.prices[date]
