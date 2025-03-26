import yfinance as yf
import pandas as pd
import numpy as np
from typing import dict

class portfolio():
  
  def __init__(self,holdings: dict, index: dict, buy_sell_signals: pd.DataFrame):
    ##
    #  Initializes a portfolio object with the following attributes:
    #  holdings: dictionary containing {ticker:amount} pairs, where ticker is the stock ticker and amount is the number of shares held
    #  index_per: dictionary containing {ticker:index_%} pairs, where index_% is the percentage of the index that the ticker represents
    #  index_cw: dictionary containing {ticker:cap_weight} pairs, where cap_weight is the capitalization weight of the ticker within the portfolio's index
    #  index: dictionary containing { 'index' : index_value}, where index_value is the total value of the portfolio's index
    #  buy_sell: DataFrame containing buy/sell signals for each stock in the portfolio retrieved from model predictions
    #  stats: dictionary containing portfolio statistics such as maximum drawdown, the corresponding recovery period, PnL, Win Loss Ratio, and possibly more to be added
    #
    ## 
    self.holdings = {} ## dict = {'ticker': amount}
    self.index_per = {} ## dict = {'ticker': index_%}
    self.index_cw = {} ## dict = {'ticker': cap_weight} 
    self.index = {} ## dict = { 'index' : index_value}
    self.buy_sell = buy_sell_signals
    self.stats = {} ## dict = {'dd_max': 0, 'dd_rec': 0}

    pass

  def add_stocks(holdings,ticker, amount, tickers: dict=None):
    '''
    Adds "amount" shares of "ticker" to the portfolio's holdings dictionary

    :param holdings: dictionary containing {ticker:amount} pairs
    :param ticker: yfinance ticker symbol for desired stock
    :param amount: number of "ticker" share to add to the portfolio
    :param tickers: optional input dictionary containing a set of {ticker:amount} pairs for convenient portfolio initialization

    '''
    if tickers != None:
      holdings.update(tickers) 
    else:
      holdings.update({ticker: amount})
      
    pass

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
    ## Data pulled includes Open, High, Low, Close, Adj_close, Volume in df format

    for ticker in holdings.keys():
      ## retrieve price data 
        price = yf.download(ticker, start= time_range[0], end=time_range[1])
        cap_weight = price * ticker.get(ticker) # calculate cap weight for each ticker, price of ticker * amount
        index_cw.update({ticker: cap_weight}) # store cap_weight in dictionary for later use 
        index.update( {"index": (cap_weight+index.get("index")) } ) # update index value for each cap_weight value

    for ticker in index_cw.keys():
        ## divide each cap_weight by index value to get index_%
        index_per.update( {ticker: (index_cw.get(ticker)*100/index.get("index")) } )
    
      
    pass
  
  def update_holdings(holdings,update):
     ''' 

     Updates the holdings dictionary with ticker:amount pairs in update dictionary created by buy/sell signals dataframe

     '''

     pass

  def update_index():
      '''
      Updates the index value and index info dictionaries with new values

      '''
      pass
  
  def update_stats():
      '''
      Updates the stats dictionary with new statistics

      '''
      pass

  def run_monte_carlo(sim_length,portfolio): ## **IN PROGRESS**
    '''
    Runs monte carlo sim for a given window into the future for given portfolio. 

    :param sim_length: integer number of time units, implied by the data, to simulate. (number of entries in sim dataframe) Defaults to 500.
    :param portfolio: portfolio object to simulate
    :return:  
    '''

    pass
  
  def past_data_sim(buy_sell,index):
     '''
     Simulates what would happen if we followed the buy/sell signals in the past market conditions.
    
     Follows buy/sell signals in the past market conditions by updating holdings and index values along the way and 
     calculating PnL and W/L at the end of the period

     '''

     pass
  
  def monte_carlo_sim():
     '''
      Simulates what would happen if we followed the buy/sell signals in the simulated future market conditions.
     '''

     pass

  def drawdown_analysis(stats,index):
      '''
      Performs Drawdown Analysis to evaluate peak-to-trough declines in the portfolio.

      :param stats: Dictionary, containing the portfolio's maximum drawdown and corresponding recovery period, to be updated
      :param index: dict with Dataframe containing the index value at each time period.
      :return: updated 'stats' dict
      '''
      ## add statistics to stats dictionary if not present
      if 'dd_max' not in stats.keys():
        stats.update({'dd_max': 0})
      if 'dd_rec' not in stats.keys():
        stats.update({'dd_rec': 0})

      ## store index[0] as intial base value
      peak = index.get(index[0]) #store index value 0
      i_peak = 0
      

      for i in range(1,len(index)):
        

        ## Check for recovery time and calculate drawdown if so. Check all Positive slope line points 
        #  to see if they are greater than the peak as this is where the recovery happens.
        # 
        #   is (in[i-1] < in[i]) and (in[i+1] > in[i])? 
        #     is index.get(index[i]) > peak?
        #     
        #       if so, i - i_peak = dd_rec
        #   
        #       Compute Drawdown
        #   
        #       find minumum index value between i_peak and i
        #       create sub data frame with index values between i_peak and i
        #       find min value in sub data frame
        #       set trough = min value
        #   
        #       dd = (peak - trough)*100/peak
        #   
        #       is dd > dd_max?
        #         if so, store this value as dd_max
        ##

        if (index.get(index[i-1]) < index.get(index[i])) and (index.get(index[i+1]) > index.get(index[i])):
          if index.get(index[i]) > peak:
            trough = min(index.get(index[i_peak:i]))
            dd = (peak - trough)*100/peak
            if dd > stats.get('dd_max'):
              dd_rec = i - i_peak
              stats.update({'dd_max' : dd})
              stats.update({'dd_rec' : dd_rec})

            pass

        ## Find local max. Find all points with negative concavity and check their relative heights
        #  
        #  is (in[i-1] < in[i]) and (in[i+1] < in[i])?
        #    is index.get(index[i]) > peak?
        #       if so, store this value as a peak and store i value(i_peak)
        #       set peak = index.get(index[i])
        ##

        if (index.get(index[i-1]) < index.get(index[i])) and (index.get(index[i+1]) < index.get(index[i])):
          if index.get(index[i]) > peak:
            peak = index.get(index[i])
            i_peak = i
        
      pass
   
   
  def win_loss_ratio(self, buy_sell):
      '''
      Calculates the Win/Loss Ratio, comparing the number of winning trades to losing trades.

      :return : float: Win/Loss ratio value.
      '''

      pass
  
  def calculate_PnL(stats,index,buy_sell):
      '''
      Profit & Loss (P&L): Track realized if we were to follow what this model predicts.

      :param index: Dataframe containing the index value at each time period.
      :param buy_sell: Dataframe containing the buy/sell signals at each time period.
      :return: float: Positive/Negative value if profit/loss was made at the end of this period
      '''

      pass
  