import yfinance as yf
import pandas as pd
import numpy as np
from typing import dict

class portfolio():
  
  def __init__(self,holdings: pd.DataFrame, index: pd.DataFrame, buy_sell_signals: pd.DataFrame):
    self._holdings = holdings ## dict = {'ticker': amount}
    self.index_per = {} ## dict = {'ticker': index_%}
    self.index_cw = {} ## dict = {'ticker': cap_weight}
    self.index = {} ## dict = { 'index' : index_value}
    self._buy_sell = buy_sell_signals
  pass

  def add_stocks(ticker, amount, tickers: dict[str,float]=default):
    """ 
    Adds "amount" shares of "ticker" to the portfolio's holdings dictionary
    :param ticker: yfinance ticker symbol for desired stock
    :param amount: number of "ticker" share to add to the portfolio
    :param tickers: optional input dictionary containing a set of ticker:amount pairs for convenient portfolio initialization
    """
    if tickers != default:
      holdings.update(tickers) 
    else:
      holdings.update({"ticker": amount})
      
  pass

  def make_index(holdings,time_range, index_comp):
    """
    Constructs a capitalization weighted index using the tickers and amounts in holdings with yfinance data
    :param holdings: dictionary containing {ticker:amount} pairs
    :param time_range: list containing [start_date, end_date] of stock data to use in index
    
    """
    
    ##Pull ticker name prices for each ticker name and construct cap_weight
    for ticker in holdings.keys():
      # retrieve price data 
        price = yf.Ticker(ticker)
        cap_weight = price * ticker.get() # calcaulte ap weight for each ticker
        index_comp.update({"ticker": cap_weight}) # store cap_weight in dictionary for later use 
        index.update( {index: (cap_weight+index.get(index)) } ) # update index value for each cap_weight value

    for ticker in index_comp.keys():
        ## divide each cap_weight by index value to get index_%
        index_per.update( {ticker: (index_comp.get(ticker)/index.get(index)) } )

    for ticker in 
    
      
  pass

  def monte_sim():
    '''
    Runs monte carlo sim for a given window into the future for given portfolio. 
  
    :param time: integer number of given time units to simulate. Defaults to 500.
    :param unit: string specifying unit of time for simulation. Options are {Monthly, Weekly, Daily, Hourly, Minutely}
                 Defaults to daily if none specified.
    :param portfolio: portfolio object to simulate
    return monte_sim
    '''
  pass
