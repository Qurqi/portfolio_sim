import pandas as pd

def drawdown_analysis(self):
    '''
    Performs Drawdown Analysis to evaluate peak-to-trough declines in the portfolio for the index and all individual stocks and update stats dataframe
    :param stats: Dataframe, containing the portfolio's maximum drawdown and corresponding recovery period, to be updated
    :param index: Dataframe containing the index value at each time period.
    '''
    ## verify dd_max and dd_rec are not NaN
    if self.stats.empty:
        self.stats = pd.DataFrame(index = ['dd_max', 'dd_rec'], columns = (self.holdings.keys(),'index'))
        self.stats.fillna(0, inplace=True)
    ## store index[0] as intial base value
        
    peak = self.index.iat[0,0] #store index value 0
    i_peak = 0
    
    for i in range(1,self.index.shape[0]):
      
      ## Check for recovery time and calculate drawdown if so. Check all Positive slope line points 
      #  to see if they are greater than the peak as this is where the recovery happens.
      if (self.index.iat[i-1,0] < self.index.iat[i,0]) and (self.index.iat[i+1,0] > self.index.iat[i,0]):
        if self.index.iat[i,0] > peak:
          trough = min(self.index.iat[i,0], self.index.iat[i_peak,0])  # Find the minimum value between peak and current index
          dd = (peak - trough)*100/peak
          if dd > self.stats.at('dd_max','index'):
            dd_rec = i - i_peak
            self.stats.at('dd_rec','index') = dd_rec
            self.stats.at('dd_max','index') = dd
          
      ## Find local max. Find all points with negative concavity and check their relative heights
      if self.index.iat[i-1,0] < self.index.iat[i,0]) and (self.index.iat[i+1,0] < self.index.iat[i,0]):
        if self.index.iat[i,0] > peak:
          peak = self.index.iat[i,0]
          i_peak = i

      for ticker in self.stats.columns:
        peak = self.data[ticker].iat[0,0] #store index value 0
        i_peak = 0
    
        for i in range(1,self.data[ticker].shape[0]):

          if (self.data[ticker].iat[i-1,0] < self.data[ticker].iat[i,0]) and (self.data[ticker].iat[i+1,0] > self.data[ticker].iat[i,0]):
            if self.data[ticker].iat[i,0] > peak:
              trough = min(self.data[ticker].iat[i,0], self.data[ticker].iat[i_peak,0])  # Find the minimum value between peak and current index
              dd = (peak - trough)*100/peak
              if dd > self.stats.at('dd_max',ticker):
                dd_rec = i - i_peak
                self.stats.at('dd_rec',ticker) = dd_rec
                self.stats.at('dd_max',ticker) = dd

          if self.data[ticker].iat[i-1,0] < self.data[ticker].iat[i,0]) and (self.data[ticker].iat[i+1,0] < self.data[ticker].iat[i,0]):
            if self.data[ticker].iat[i,0] > peak:
              peak = self.data[ticker].iat[i,0]
              i_peak = i

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
