from typing import Dict
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime
import time

class portfolio:

    def __init__(self,holdings: Dict,buy_sell_signals: pd.DataFrame):
        ##
        #  Initializes a portfolio object with the following attributes:
        #
        #  :param holdings: dictionary containing {ticker:{amount:date_range} } triplets, where ticker is the stock ticker and amount is the number of shares held, and date_range is the range of dates which we wnt to 
        #  :param index_per: dictionary containing {ticker:index_%} pairs, where index_% is the percentage of the index that the ticker represents
        #  :param index_cw: dictionary containing {ticker:cap_weight} pairs, where cap_weight is the capitalization weight of the ticker within the portfolio's index
        #  :param index: dictionary containing { 'index' : index_value}, where index_value is the total value of the portfolio's index
        #  :param buy_sell: DataFrame containing buy/sell signals for each stock in the portfolio retrieved from model predictions
        #  :param stats: dictionary containing portfolio statistics such as maximum drawdown, the corresponding recovery period, PnL, Win Loss Ratio, and possibly more to be added
        ## 
        if holdings == None:
            self.holdings = {} ## dict = {'ticker': {amount:date_range} } nested dictionaries with ticker amount and date_range groups
        else:
            self.holdings = holdings

        self.index_per = {} ## dict = {'ticker': index_%}
        self.index_cw = {} ## dict = {'ticker': cap_weight} 
        self.index = {'index':0.0} ## dict = { 'index' : index_value}
        self.buy_sell = buy_sell_signals
        self.stats = {} ## dict = {'dd_max': 0, 'dd_rec': 0, ...} stats for index
        self.data = {} ## dict = {'ticker': DataFrame} where DataFrame contains stock data for ticker, including Open, High, Low, Close, Adj_close, Volume

    def add_stocks(self, ticker, amount, tickers: Dict = None):
           '''
           Adds "amount" shares of "ticker" to the portfolio's holdings dictionary

           :param holdings: dictionary containing {ticker:amount} pairs
           :param ticker: yfinance ticker symbol for desired stock
           :param amount: number of "ticker" share to add to the portfolio
           :param tickers: optional input dictionary containing a set of {ticker:amount} pairs for convenient portfolio initialization

           '''
           if tickers != None:
               self.holdings.update(tickers)
           else:
               self.holdings.update({ticker: amount})
   


    def make_index(index,index_cw,index_per,holdings,time_range):
        '''
        Constructs a capitalization weighted index using the tickers and amounts in holdings with yfinance data

        :param index: dictionary containing { 'index' : index_value}
        :param index_cw: dictionary containing {ticker:cap_weight} pairs
        :param index_per: dictionary containing {ticker:index_%} pairs
        :param holdings: dictionary containing {ticker:amount} pairs
        :param time_range: 2 entry list containing [start_date, end_date] of stock data to use in index. 
                          start date and end_date must be in the format 'YYYY-MM-DD'

        '''

        ## Pull prices for each ticker name and construct cap_weight, index, and index_% dictionaries
        ## Data pulled in df format
       

    def update_holdings(self, update: Dict):
        '''   
        Updates the holdings dictionary with ticker:amount pairs in update dictionary 

        '''
        pass

    def update_index(self):
        '''
        Updates the index value and index info dictionaries with new values 

        '''  
        pass

    def update_stats(self):
        '''
        Updates the stats dictionary with new statistics 

        '''
        pass