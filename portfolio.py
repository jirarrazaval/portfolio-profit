from datetime import datetime
from stock import Stock
from typing import List

class Portfolio:
  def __init__(self, name):
    self.name = name
    self.stocks = []

  def __str__(self):
    return f'{self.name}: {self.profit()}'
  
  def add(self, stocks: List[Stock]):
    self.stocks.extend(stocks)

  def remove(self, stocks: List[Stock]):
    for stock in stocks:
      self.stocks.remove(stock)

  def profit(self, start_date, end_date, annualized=False):
    total_profit = 0
    initial_value = 0

    for stock in self.stocks:
        initial_price = stock.price(start_date)
        final_price = stock.price(end_date)
        total_profit += final_price - initial_price
        initial_value += initial_price

    if annualized and initial_value > 0:
        days = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days
        return (total_profit / initial_value) * (365 / days)
    
    return total_profit


  
