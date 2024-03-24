import os
import requests
import datetime
from bs4 import BeautifulSoup as bs

class Stock:
    
    def __init__(self,stk_no, name, srch_rate, n_p, ysd_p, ud_r, tr_a, st_p, hi_p, low_p, per, roe) -> None:
        
        self.stockNo = stk_no
        self.name = name
        self.search_rate = srch_rate
        self.now_price = n_p
        self.yesterday_price = ysd_p
        self.up_down_rate = ud_r
        self.trade_amount = tr_a
        self.start_price = st_p
        self.high_price = hi_p
        self.low_price = low_p
        self.PER = per
        self.ROE = roe

        self.list = [self.stockNo, self.name, self.search_rate, self.now_price, self.yesterday_price, self.up_down_rate, self.trade_amount,
                     self.start_price, self.high_price, self.low_price, self.PER, self.ROE]
    def __str__(self):
        return '{}  {}  {} {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(*self.list)
                

# ready to crawling from web

# set url

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs(res.text, 'html.parser')

# find stock data

title_list = list(map(lambda x : x.text, soup.select('tr th')))

stock = soup.select('tr')
stock_list = stock[7:]

# remove useless tag
re_stock_list = []
for stock in stock_list:
    if 'class="no"' in str(stock):
        re_stock_list.append(stock)
        
# remove blank
new_stocks = []
for new_stock in re_stock_list:
    new_stock = new_stock.find_all('td')
    for idx, data in enumerate(new_stock):
        new_stock[idx] = data.text.strip()
    new_stocks.append(new_stock)


stocks = [Stock(*stock) for stock in new_stocks]
print(datetime.datetime.now())
print(*title_list, sep='   ')
for stock in stocks:
    print(stock)