from portfolio import Portfolio
from stock import Stock

stock1 = Stock('TSLA', {'2021-01-01': 100, '2021-01-02': 200})
stock2 = Stock('AAPL', {'2021-01-01': 400, '2021-01-02': 600})
portfolio = Portfolio('Tech')
portfolio.add([stock1, stock2])

profit = portfolio.profit('2021-01-01', '2021-01-02')
print(f"Profit: {profit}")

annualized_profit = portfolio.profit('2021-01-01', '2021-01-02', annualized=True)
print(f"Annualized Profit: {annualized_profit}")