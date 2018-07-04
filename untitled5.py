# -*- coding: utf-8 -*-
"""
Created on Wed Jul 04 12:08:50 2018

@author: ABHIBASU SEN
"""

import bs4 as bs
import pickle
import requests

def save_nifty50_tickers():
    resp=requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup=bs.BeautifulSoup(resp.text,"lxml")
    table=soup.find('table', {'class':'wikitable sortable'})
    tickers=[]
    for row in table.findAll('tr')[1:]:
        ticker= row.findAll('td')[1].text
        tickers.append(ticker)
    with open("nifty50.pickle","wb") as f:
        pickle.dump(tickers,f)
    print (tickers)
    return tickers
save_nifty50_tickers() 