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
        #  :param holdings: dictionary containing {ticker: amount} pairs, where ticker is the stock ticker and amount is the number of shares held
        #  :param index: dataframe containing the indexes closing price data. the column name is index
        #  :param buy_sell: DataFrame containing buy/sell signals for each stock in the portfolio retrieved from model predictions
        #  :param data: dataframe containing the closing price data for each stock in the portfolio. ticker names are the column names
        #  :param stats: dictionary containing portfolio statistics such as maximum drawdown, the corresponding recovery period, PnL, Win Loss Ratio, 
        #                and the capitalization weight of each stock in the portfolio. Stat names are the indexes and ticker names are the column names
        ## 
        if holdings.empty:
            self.holdings = {}
        else:
            self.holdings = holdings
        self.index = pd.DataFrame(columns = ['index']) ## DataFrame to hold the index of the portfolio
        self.buy_sell = buy_sell_signals
        self.data = pd.DataFrame()
        self.stats = pd.DataFrame(index = ['dd_max', 'dd_rec', 'PnL', 'win_loss_ratio','index_percent']) # append more stats as we add them


    def add_stocks(self, ticker, amount, tickers: Dict = None):
           '''
           Adds "amount" shares of "ticker" to the portfolio's holdings dictionary

           :param holdings: dictionary containing {ticker:amount} pairs
           :param ticker: yfinance ticker symbol for desired stock
           :param amount: number of "ticker" share to add to the portfolio
           :param tickers: optional input dictionary containing a set of {ticker:amount} pairs for convenient portfolio initialization

           '''
           


    def make_index(self,time_range):
        '''
        Constructs a capitalization weighted index using the tickers and amounts in holdings with yfinance data
        :param time_range: list containing the start and end dates for the index data in the format [start_date, end_date]

        '''

        ## Pull prices for each ticker name and construct cap_weight, index, and index_% dictionaries
        ## Data pulled in df format

   
        for ticker in self.holdings.keys():
            price = yf.download(ticker, start= time_range[0], end=time_range[1]) ## retrieve price data 
            price = price['Close'].rename({'Close':ticker}) ## rename the column to the ticker name
            cap_weight = price[ticker].mul(self.holdings.get(ticker)) ## calculate cap weight for the ticker, price of ticker * amount
            cap_weight = cap_weight.rename({ticker: 'index'})
            if self.data.empty: ## if data DataFrame is empty, initialize it with the ticker and price
                self.data = pd.DataFrame(price)
            else:
                self.data.insert(self.data.shape[1],ticker,price[ticker]) ## add the price data to the data DataFrame

            if self.index.empty: ## add cap_weight to index DataFrame
                self.index = cap_weight
            else:
                self.index = self.index.add(cap_weight)
        


    def update_holdings(self, update: Dict):
        '''   
        Updates the holdings dictionary with ticker:amount pairs in update dictionary 

        '''


        pass

    def update_index(self):
        '''
        Updates the index value

        '''  
        # given new holdings, update the index value by recalculating the capitalization weighted index
        
        #clear index DataFrame
        self.index = pd.DataFrame(columns=['index'])
        # Recalculate the index with the current holdings using the existing data
        for ticker in self.holdings.keys():
            price = self.data[ticker]
            cap_weight = price.mul(self.holdings.get(ticker))
            cap_weight = cap_weight.rename({ticker: 'index'})
            if self.index.empty:
                self.index = cap_weight
            else:
                self.index = self.index.add(cap_weight)
    

    def update_stats(self):
        '''
        Updates the stats dictionary with new statistics 

        '''
        pass
