import yfinance as yf
import pandas as pd
import numpy as np
from typing import dict

class portfolio():
  
  def __init__(self,holdings: dict, index: dict, buy_sell_signals: pd.DataFrame):
    self.holdings = {} ## dict = {'ticker': amount}
    self.index_per = {} ## dict = {'ticker': index_%}
    self.index_cw = {} ## dict = {'ticker': cap_weight}
    self.index = {} ## dict = { 'index' : index_value}
    self.buy_sell = buy_sell_signals
    pass

  def add_stocks(holdings,ticker, amount, tickers: dict=None):
    """ 
    Adds "amount" shares of "ticker" to the portfolio's holdings dictionary

    :param holdings: dictionary containing {ticker:amount} pairs
    :param ticker: yfinance ticker symbol for desired stock
    :param amount: number of "ticker" share to add to the portfolio
    :param tickers: optional input dictionary containing a set of {ticker:amount} pairs for convenient portfolio initialization

    """
    if tickers != None:
      holdings.update(tickers) 
    else:
      holdings.update({ticker: amount})
      
    pass

  def make_index(index,index_cw,index_per,holdings,time_range):
    """
    Constructs a capitalization weighted index using the tickers and amounts in holdings with yfinance data

    :param index: dictionary containing { 'index' : index_value}
    :param index_cw: dictionary containing {ticker:cap_weight} pairs
    :param index_per: dictionary containing {ticker:index_%} pairs
    :param holdings: dictionary containing {ticker:amount} pairs
    :param time_range: 2 entry list containing [start_date, end_date] of stock data to use in index. 
                      start date and end_date must be in the format 'YYYY-MM-DD'
    
    """
    
    ## Pull prices for each ticker name and construct cap_weight, index, and index_% dictionaries
    ## Data pulled includes Open, High, Low, Close, Adj_close, Volume in df format

    for ticker in holdings.keys():
      # retrieve price data 
        price = yf.download(ticker, start= time_range[0], end=time_range[1])
        cap_weight = price * ticker.get(ticker) # calculate cap weight for each ticker, price of ticker * amount
        index_cw.update({ticker: cap_weight}) # store cap_weight in dictionary for later use 
        index.update( {"index": (cap_weight+index.get("index")) } ) # update index value for each cap_weight value

    for ticker in index_cw.keys():
        ## divide each cap_weight by index value to get index_%
        index_per.update( {ticker: (index_cw.get(ticker)*100/index.get("index")) } )
    
      
    pass

  def monte_sim():
      '''
      Runs monte carlo sim for a given window into the future for given portfolio. 

      :param time: integer number of given time units to simulate. Defaults to 500.
      :param unit: string specifying unit of time for simulation. Options are {Monthly, Weekly, Daily, Hourly, Minutely}
                   Defaults to daily if none specified.
      :param portfolio: portfolio object to simulate
      :return:  dataframe containing the simulated portfolio value at each time period
      '''
      pass

  def calculate_PnL(index,buy_sell):
      """
      Profit & Loss (P&L): Track realized if we were to follow what this model predicts.

      :param index: Dataframe containing the index value at each time period.
      :param buy_sell: Dataframe containing the buy/sell signals at each time period.

      :return: float: Positive/Negative value if profit/loss was made at the end of this period
      """
      pass
  
  def drawdown_analysis(index):
      """
      Performs Drawdown Analysis to evaluate peak-to-trough declines in the portfolio.
      :return: dict: Dictionary containing drawdown statistics such as maximum drawdown and recovery period.
      """
      pass
   
   
  def win_loss_ratio(self, buy_sell):
      """
      Calculates the Win/Loss Ratio, comparing the number of winning trades to losing trades.
      :return : float: Win/Loss ratio value.
      """
      pass
  