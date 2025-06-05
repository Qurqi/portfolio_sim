
import pandas as pd
import portfolio.portfolio as pf
import numpy as np
import scipy.stats as stats


def drawdown_analysis(self):
    '''
    Performs Drawdown Analysis to evaluate peak-to-trough declines in the portfolio for the index and all individual stocks and update stats dataframe
    :param stats: Dataframe, containing the portfolio's maximum drawdown and corresponding recovery period, to be updated
    :param index: Dataframe containing the index value at each time period.
    '''
    if self.stats.index.name != 'dd_max':
      #append 0 row to stats dataframe
      self.stats = self.stats._append(pd.Series(name='dd_max'))
      self.stats.loc['dd_max'] = 0.0  # Initialize the dd_max row with zeros for all tickers
    if self.stats.index.name != 'dd_rec':
      #append 0 row to stats dataframe
      self.stats = self.stats._append(pd.Series(name='dd_rec'))
      self.stats.loc['dd_rec'] = 0.0  # Initialize the dd_max row with zeros for all tickers

    
    for ticker in self.stats.columns:  
      peak = self.data[ticker].iat[0] #store index value 0
      i_peak = 0
  
      for i in range(1,self.data[ticker].shape[0]-1):
        
        if (self.data[ticker].iat[i-1] < self.data[ticker].iat[i]) and (self.data[ticker].iat[i+1] > self.data[ticker].iat[i]):
          if self.data[ticker].iat[i] > peak:
        
            trough = min(self.data[ticker].iloc[i_peak:i])  # Find the minimum value between peak and current index
            dd = (peak - trough)*100.0/peak
            
            if dd > self.stats.at['dd_max',ticker]:
              dd_rec = i - i_peak
              self.stats.at['dd_rec',ticker] = dd_rec 
              self.stats.at['dd_max',ticker] = dd
        if (self.data[ticker].iat[i-1] < self.data[ticker].iat[i]) and (self.data[ticker].iat[i+1] < self.data[ticker].iat[i]):
          if self.data[ticker].iat[i] > peak:
            peak = self.data[ticker].iat[i]
            i_peak = i

def win_loss_ratio(self):
    '''
    Calculates the Win/Loss Ratio, comparing the number of winning trades to losing trades.
    :return : float: Win/Loss ratio value.
    '''
    if self.stats.index.name != 'win_loss_ratio':
      #append 0 row to stats dataframe
      self.stats = self.stats._append(pd.Series(name='win_loss_ratio'))
      self.stats.loc['win_loss_ratio'] = 0.0  # Initialize the win_loss_ratio row with zeros for all tickers
    pass
  
def calculate_PnL(self):
    '''
    Profit & Loss (P&L): Track realized if we were to follow what this model predicts.

    :param index: Dataframe containing the index value at each time period.
    :param buy_sell: Dataframe containing the buy/sell signals at each time period.
    :return: float: Positive/Negative value if profit/loss was made at the end of this period

    '''
    if self.stats.index.name != 'win_loss_ratio':
      #append 0 row to stats dataframe
      self.stats = self.stats._append(pd.Series(name='win_loss_ratio'))
      self.stats.loc['win_loss_ratio'] = 0.0  # Initialize the win_loss_ratio row with zeros for all tickers
      
    pass

def check_stationarity(self):
    '''
    Check if the time series data is stationary using the Augmented Dickey-Fuller test.
    :return: bool: True if the time series is stationary, False otherwise.
    '''
    # Perform the Augmented Dickey-Fuller test
    result = stats.adfuller(self.data['index'])
    
    # Check the p-value
    if result[1] < 0.05:
        return True  # Time series is stationary
    else:
        return False  # Time series is not stationary
    
def 

