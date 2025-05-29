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

        :param index: dictionary containing { 'index' : index_value}
        :param index_cw: dictionary containing {ticker:cap_weight} pairs
        :param index_per: dictionary containing {ticker:index_%} pairs
        :param holdings: dictionary containing {ticker:amount} pairs
        :param time_range: 2 entry list containing [start_date, end_date] of stock data to use in index. 
                           start date and end_date must be in the format 'YYYY-MM-DD'

        '''
        pass


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
